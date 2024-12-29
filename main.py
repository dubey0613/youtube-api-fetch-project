from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.video import Video
import requests
from datetime import datetime, timedelta
from config import Config
from flask_cors import CORS
from utils import paginate, build_youtube_url

app = Flask(__name__)
CORS(app)
# Load the configuration
app.config.from_object(Config)

# Access environment variables
YOUTUBE_API_KEY = app.config['YOUTUBE_API_KEY']
DATABASE_URL = app.config['DATABASE_URL']

# Initialize SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Initialize the background scheduler
scheduler = BackgroundScheduler()

SEARCH_QUERY = "cricket"

def fetch_latest_videos():
    published_after = (datetime.utcnow() - timedelta(days=1)).isoformat() + "Z"

    url = build_youtube_url(SEARCH_QUERY, YOUTUBE_API_KEY, published_after)    
    response = requests.get(url)
    
    if response.status_code == 200:
        videos = response.json().get('items', [])
        
        existing_video_ids = set(
            video.video_id for video in session.query(Video).all()
        )
        
        for video in videos:
            video_id = video['id']['videoId']
            
            # Skip videos that are already in the database
            if video_id in existing_video_ids:
                print(f"Video already exists: {video['snippet']['title']}")
                continue
            
            title = video['snippet']['title']
            description = video['snippet']['description']
            published_at = video['snippet']['publishedAt']
            thumbnails = video['snippet']['thumbnails']['high']['url']
            
            new_video = Video(
                video_id=video_id,
                title=title,
                description=description,
                published_at=published_at,
                thumbnails=thumbnails
            )
            session.add(new_video)
            session.commit()
            print(f"Inserted video: {title}")
    else:
        print("Error fetching data from YouTube API")


# Schedule the background task to run every 10 seconds
scheduler.add_job(fetch_latest_videos, 'interval', seconds=10)

# Start the scheduler
scheduler.start()

@app.route('/test-db', methods=['GET'])
def test_db_connection():
    try:
        result = session.query(Video).all()
        if result:
            return jsonify({"message": "Database connection successful!", "data": [video.__repr__() for video in result]}), 200
        else:
            return jsonify({"message": "No data found!"}), 404
    except Exception as e:
        return jsonify({"error": f"Database connection failed: {str(e)}"}), 500
    


@app.route('/get-youtube-video-details', methods=['GET'])
def get_videos():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        session = Session()

        # Fetch videos sorted by publishedAt in descending order
        query = session.query(Video).order_by(Video.published_at.desc())

        # Paginate the query
        paginated_videos = paginate(query, page, per_page)

        videos_data = [{
            'video_id': video.video_id,
            'title': video.title,
            'description': video.description,
            'publishedAt': video.published_at.isoformat()
        } for video in paginated_videos]

        session.close()

        return jsonify({
            'page': page,
            'per_page': per_page,
            'videos': videos_data
        }), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch videos: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
