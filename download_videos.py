import os
from pytube import YouTube

DOWNLOAD_PATH = "."
API_KEY = ""

with open('keywords.txt', 'r') as f:
	keywords = [keyword.strip() for keyword in f.readlines()]

for keyword in keywords:
	print (keyword)
	try:
		os.system('python python-youtube-api/main.py --s --search "%s" --max 50 --key %s' % (keyword, API_KEY))
	except Exception as e:
		pritn (e, keyword)
	with open('output/search_term_videos.csv', 'r') as f:
		f.readline()
		lines = f.readlines()
	os.makedirs('{}/{}'.format(DOWNLOAD_PATH, "_".join(keyword.split())), exist_ok=True)
	path = '{}/{}'.format(DOWNLOAD_PATH, "_".join(keyword.split()))
	count = 0
	for line in lines:
		videoID = (line.split(',')[-3])
		try:
			yt = YouTube("https://www.youtube.com/watch?v=%s" % (videoID))
			yt.streams.filter(res="720p").first().download(output_path=path, filename="{}".format(videoID))
			count += 1
			if count > 50:
				break
		except Exception as e:
			print (e, videoID)