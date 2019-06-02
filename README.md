# WhatsApp-Group-Analyzer
Automatically generates Charts and a Report from your WhatsApp Group Chat

![Example1](https://github.com/viniciusov/WhatsApp-Group-Analyzer/blob/master/sample_images/pic1.png)
![Example2](https://github.com/viniciusov/WhatsApp-Group-Analyzer/blob/master/sample_images/pic2.png)

## Requirements
- Python 3 installed in your OS (Instructions about Installation in https://realpython.com/installing-python/)
- In your Terminal or Command Prompt, run `pip install numpy matplotlib pandas` to install the required libraries

## How Use it

#### 1. Export your WhatsApp Group Chat
- For Android -> https://faq.whatsapp.com/en/android/23756533/
- For Iphone -> https://faq.whatsapp.com/en/iphone/20888066
- For Windows Phone -> https://faq.whatsapp.com/en/wp/22548236

#### 2. Move the Exported .txt file to the WhatsApp-Group-Analyzer folder
  
#### 3. Rename it to `Chat.txt`

#### 4. Click on `Analyzer.py` file or run `python3 Analyzer.py` in your Terminal or Command Prompt
*Try 'python Analyzer.py' if you get an error.*

#### 5. Now you should have 3 generated files in the same folder:
- `pic1.png` -> A Bar Chart showing the number of messages sent by each group user
- `pic1.png` -> A Pie Chart showing the number of sent messages (in percentage) by users who have more than 10% of participation
- `pic1.png` -> A Report showing the number of messages by each user

*For privacy reasons the telephone numbers in the sample_images folder have been hidden.*

## License
This project is under GPLv3 license.

## Contact
If you have any doubt, suggestions or want to contact me, use my email viniciusov@hotmail.com.
