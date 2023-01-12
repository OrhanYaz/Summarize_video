Here is a litle personnal project i built to summarize youtube videos

It uses yt-dlp package to download youtube video as mp3 (only need audio for next step).
Then it uses Whisper from openAI as speech-to-text framework to convert audio file into text.
At last step, we uses facebook/bart-large-cnn to summarize the text using huggingface transformers.


There is one problem now: the summary model takes maximum 1024 token so we can only fully summarize small videos otherwise the model will truncate the input taxt to match maximum token.



yt-dlp: https://github.com/yt-dlp/yt-dlp
whisper: https://openai.com/blog/whisper/
huggingface - bart: https://huggingface.co/facebook/bart-large-cnn
