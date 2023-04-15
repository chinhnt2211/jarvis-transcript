from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_transcript():
    video_url = request.form['video_url']
    video_id = video_url.split('=')[1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['en'])
    api_transcript= transcript.fetch()
    

    text_transcript = ""
    for each in api_transcript:
        text_transcript = text_transcript + " " + each["text"] 

    return render_template('index.html', transcript=text_transcript)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


        
        
