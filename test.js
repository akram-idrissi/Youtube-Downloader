const ytdl = require('ytdl-core');
const fs = require('fs');
const path = require('path');

async function downloadVideo(videoUrl, outputDir) {
    try {
        const videoInfo = await ytdl.getInfo(videoUrl);
        const videoTitle = videoInfo.videoDetails.title.replace(/[/\\?%*:|"<>]/g, ''); 
        const outputFilePath = path.join(outputDir, `${videoTitle}.mp3`);

        const audioStream = ytdl(videoUrl, { quality: 'highestaudio' })
            .on('end', () => {
                console.log(`Downloaded and converted to MP3: ${videoTitle}`);
            });

        audioStream.pipe(fs.createWriteStream(outputFilePath));
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
}

if (process.argv.length < 4) {
    console.error('Usage: node download.js <video_url> <output_directory>');
} else {
    const videoUrl = process.argv[3];
    const outputDir = process.argv[2];

    downloadVideo(videoUrl, outputDir);
}
