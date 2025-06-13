# Using MAVIS 3  

<div align="left">
   <img alt="mavis" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-icon-banner-3.svg">
   <img alt="mavis-launcher" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-launcher-icon-banner-3.svg">
   <img alt="mavis-terminal" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-terminal-icon-banner-3.svg">
   <img alt="tg-loerrach" src="https://img.shields.io/badge/TG Lörrach-red?style=flat">
   <img alt="peharge" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/Peharge-icon-banner-3.svg">
</div>

## 1. Launching the MAVIS Installer  
To begin the installation process, execute the appropriate [`mavis-launcher-4.bat`](https://github.com/Peharge/MAVIS/blob/main/mavis-launcher-4.bat) file for your desired MAVIS version. This will open a terminal window on your operating system, initiating the MAVIS Installer.
```bash
Aktive Codepage: 65001.

-------------------------------------------------
       Welcome to the MAVIS Launcher 4
-------------------------------------------------
     Initiating high-tech installation...
          Prepare for the next level

                 MIT License
             Copyright (c) 2024
                   Peharge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Gooo...

✅ Python is already installed.
✅ Git is already installed.
✅ Ollama is already installed.
✅ FFmpeg is already installed.
✅ Rustup is already installed.
MAVIS repository already exists. Checking for updates...
Fetching latest changes...
Updates available, pulling changes...
✅ MAVIS repository updated successfully
✅ MAVIS update process completed successfully.
✅ .env file already exists.
✅ Starting MAVIS...
✅ All tasks were completed successfully

Ollama is installed.
Ollama is already running.

All MAVIS versions are available here:

III Required LLM model for this MAVIS version is already installed
III Required LLM model for this MAVIS version is not yet installed
III LLM model is available for you - you have all the permissions
III LLM model is not available for you - you do not have permission to install the model

1. MAVIS 3:
   - mavis-3-main: With Xc++ 3 11B or Llama3.2 11B + Phi4 14b + Qwen 2.5 1.5b + granite3.2-vision 2b (phi4 Not Installed)
   - mavis-3-main-mini: With Xc++ 3 11B or Llama3.2 11B + Phi4-mini 3.8b + Qwen 2.5 1.5b + granite3.2-vision 2b (phi4-mini Not Installed)
   - mavis-3-math: With Xc++ 3 11B or Llama3.2 11B + DeepSeek R1 14b + Qwen 2.5 1.5b + granite3.2-vision 2b (deepseek-r1:14b Installed)
   - mavis-3-math-pro: With Xc++ 3 11B or Llama3.2 11B + DeepSeek R1 32b + Qwen 2.5 1.5b + granite3.2-vision 2b (deepseek-r1:32b Not Installed)
   - mavis-3-math-ultra: With Xc++ 3 11B or Llama3.2 90B + DeepSeek R1 671b + Qwen 2.5 1.5b + granite3.2-vision 2b (deepseek-r1:671b Not Installed)
   - mavis-3-math-mini: With Xc++ 3 11B or Llama3.2 11B + DeepSeek R1 7b + Qwen 2.5 1.5b + granite3.2-vision 2b (deepseek-r1:7b Not Installed)
   - mavis-3-math-mini-mini: With Xc++ 3 11B or Llama3.2 11B + DeepSeek R1 1.5b + Qwen 2.5 1.5b + granite3.2-vision 2b (deepseek-r1:1.5b Not Installed)
   - mavis-3-code: With Xc++ 3 11B or Llama3.2 11B + Qwen 2.5 Coder 14B + Qwen 2.5 1.5b + granite3.2-vision 2b (qwen2.5-code:14b Not Installed)
   - mavis-3-code-pro: With Xc++ 3 11B or Llama3.2 11B + Qwen 2.5 Coder 32B + Qwen 2.5 1.5b + granite3.2-vision 2b (qwen2.5-code:32b Not Installed)
   - mavis-3-code-mini: With Xc++ 3 11B or Llama3.2 11B + Qwen 2.5 Coder 7B + Qwen 2.5 1.5b + granite3.2-vision 2b (qwen2.5-code:7b Not Installed)
   - mavis-3-code-mini-mini: With Xc++ 3 11B or Llama3.2 11B + Qwen 2.5 Coder 1.5B + Qwen 2.5 1.5b + granite3.2-vision 2b (qwen2.5-code:1.5b Not Installed)

2. MAVIS 3.3:
   - mavis-3-3-main: With Xc++ 3 11B or Llama3.2 11B + Gemma3 12B + Qwen 2.5 1.5b + granite3.2-vision 2b (gemma3:12b Installed)
   - mavis-3-3-main-pro: With Xc++ 3 11B or Llama3.2 11B + Gemma3 27B + Qwen 2.5 1.5b + granite3.2-vision 2b (gemma3:27b Not Installed)
   - mavis-3-3-main-mini: With Xc++ 3 11B or Llama3.2 11B + Gemma3 4B + Qwen 2.5 1.5b + granite3.2-vision 2b (gemma3:4b Installed)
   - mavis-3-3-main-mini-mini: With Xc++ 3 11B or Llama3.2 11B + Gemma3 1B + Qwen 2.5 1.5b + granite3.2-vision 2b (gemma3:1b Installed)
   - mavis-3-3-math: With Xc++ 3 11B or Llama3.2 11B + QwQ 32b + Qwen 2.5 1.5b + granite3.2-vision 2b (qwq Not Installed)
   - mavis-3-3-math-mini: With Xc++ 3 11B or Llama3.2 11B + DeepScaleR 1.5b + Qwen 2.5 1.5b + granite3.2-vision 2b (deepscaler Installed)

3. MAVIS fast start:
   - mavis-3-main-fast: With Xc++ 3 11B or Llama3.2 11B + Phi4 14b + Qwen 2.5 1.5b + granite3.2-vision 2b (phi4 Not Installed)
   - mavis-3-math-fast: With Xc++ 3 11B or Llama3.2 11B + DeepSeek R1 14b + Qwen 2.5 1.5b + granite3.2-vision 2b (deepseek-r1:14b Installed)
   - mavis-3-code-fast: With Xc++ 3 11B or Llama3.2 11B + Qwen 2.5 Coder 14B + Qwen 2.5 1.5b + granite3.2-vision 2b (qwen2.5-code:14b Not Installed)
   - mavis-3-3-main-fast: With Xc++ 3 11B or Llama3.2 11B + Gemma3 12B + Qwen 2.5 1.5b + granite3.2-vision 2b (gemma3:12b Installed)
   - mavis-3-3-math-fast: With Xc++ 3 11B or Llama3.2 11B + QwQ 32b + Qwen 2.5 1.5b + granite3.2-vision 2b (qwq Not Installed)

4. MAVIS Terminal 3 EAP:
   - mavis-terminal: The MAVIS Terminal is always available for you!!! ( Installed)

5. MAVIS 4 EAP:
   - mavis-4: NEW - Development of MAVIS 4 has begun – featuring new Vision Models, a more powerful and faster MAVIS Terminal, and access to over 200 models. ( Installed)

6. MAVIS Terminal 4 EAP:
   - mavis-terminal-4: The MAVIS Terminal is always available for you!!! ( Installed)

Enter a MAVIS batch file (e.g. 'mavis-4', 'mavis-3-code' or 'mavis-terminal-4'):
```

If you are launching MAVIS 3 for the first time, the installation process may take between **10 to 30 minutes**, depending on your internet speed. If MAVIS is already installed, the program will start in approximately **5 seconds**.  

Regardless of the installation state, the system will always perform a **completeness check** and apply updates if necessary.

If you are starting **MAVIS 3 for the first time**, please **do not select** the **"3. MAVIS 3 EAP Fast Start"** option. Instead, choose one of the following:  

- **"1. MAVIS 3 EAP"**  
- **"2. MAVIS Terminal 3 EAP"** *(Recommended for experienced users only. More information: [MAVIS Terminal Guide](https://github.com/Peharge/MAVIS/blob/main/learn-mavis/learn-mavis-terminal-3.md))*

After entering the desired MAVIS version, such as `"mavis-3-code"`, the specified program will launch automatically.  

```bash
Enter a MAVIS batch file (e.g. 'mavis-3-code'):mavis-3-code
Executing file: C:\Users\julia\PycharmProjects\MAVIS\run-mavis-3-code.bat

      ██╗     █╗
     ████╗   ███╗        ███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗    ██████╗      ██████╗ ██████╗ ██████╗ ███████╗
    ██████╗  ████╗       ████╗ ████║██╔══██╗██║   ██║██║██╔════╝    ╚════██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
   ████████╗  ████╗      ██╔████╔██║███████║██║   ██║██║███████╗     █████╔╝    ██║     ██║   ██║██║  ██║█████╗
  ████╔█████╗  ████╗     ██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║     ╚═══██╗    ██║     ██║   ██║██║  ██║██╔══╝
 ████╔╝ █████╗  ████╗    ██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║    ██████╔╝    ╚██████╗╚██████╔╝██████╔╝███████╗
 ╚═══╝   ███╔╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝    ╚═════╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
          █╔╝
          ╚╝

A warm welcome, Mr.X, to MAVIS (MAth Visual Intelligent System) - the most powerful calculator in the world!
Developed by Peharge and JK (Peharge Projects 2025)
Thank you so much for using MAVIS. We truly appreciate your support ❤️

MAVIS Version: 3
MAVIS Installer Version: 3
MAVIS Terminal Version: 3
MAVIS License: MIT

████████
████████

Framework Information:
----------------------
Do you want to install or update the required Python frameworks for MAVIS? [y/n]:
```

## 2. Installing the required frameworks
Once the terminal is opened, a list of Python frameworks required for MAVIS will appear. These frameworks allow MAVIS to perform various tasks. You can also use them later in Jupyter Notebook, as MAVIS runs in its own Python environment.

For example, the output might look like this:

```bash
Framework Information:
----------------------
Do you want to install or update the required Python frameworks for MAVIS? [y/n]:y

Flask - Lightweight web framework for Python.
Ollama - Tool for integrating with AI APIs.
Jupyter - Open source web application for live code, equations, visualizations and text.
etc.
```

You will also see the following message reminding you that you should update PIP occasionally:

```bash
Dont forget to update PIP regularly with the command: python -m pip install --upgrade pip.
```

If not already done, the required frameworks will now be installed and updated:

```bash
All frameworks for MAVIS versions 1.2, 1.3, 1.4 and 1.5 are currently being installed and updated:
```

If you are starting MAVIS for the first time, you will need to confirm that each framework should be installed. Enter `y` or `yes` to start the installation:

```bash
Would you like to install Flask? [y/n]:
```

Please always confirm with `y` or `yes` to avoid later problems. The same applies to future automatic updates of the frameworks.

## 3. Updating MAVIS
After installing the frameworks, you will be asked if you want to update MAVIS. The latest version will be downloaded from GitHub. The automatic update is usually stable, but errors can occur. If you experience problems, use this command manually:

```bash
git pull https://github.com/Peharge/MAVIS.git
```

The update query looks like this:

```bash
MAVIS Repository Update (experimental):
--------------------------------------
This update function is not yet 100% reliable and errors may occur.
We therefore recommend using the command:
git pull https://github.com/Peharge/MAVIS.git
instead.

MAVIS - Last update: 01/30/2025
Would you like to perform an update? [y/n]:
```

## 4. Installation of additional AI models
After the update, two AI models must be installed. These must each be confirmed with `y` or `yes`.

Some system information will then appear that does not necessarily need to be understood in order to use MAVIS.

## 5. Starting Jupyter Notebook
After a short while, another terminal will open, asking you if you want to open Jupyter Notebook. Jupyter Notebook is a code editor that runs in the browser and is installed with MAVIS.

```bash
Do you want to start Jupyter Notebook? [y/n]:
```

If you enter `y` or `yes`, Jupyter Notebook will open in the browser.

Regardless of this selection, MAVIS will automatically open in a browser tab. If the browser has not started, a connection error may be displayed. This is because the MAVIS server needs a little longer to start up than the browser. In this case, wait 15-30 seconds and refresh the tab. The first start may take a little longer depending on the PC performance.

After the successful start, your browser should look like this:

![MAVIS](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/using-img-1.png)

## 6. Using MAVIS
You can now send questions to the chatbot, upload images and use the control panel.

![Using MAVIS](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/using-img-2.png)

Once you have uploaded an image, a small window will appear with the image. Simply click on the window to close it.

If you want to ask the chatbot to create a graph, tell it to use one of the following frameworks:
- Matplotlib
- Plotly
- Seaborn
- Altair

MAVIS also supports LaTeX for mathematical formulas and can perform calculations directly.

Here is an example of MAVIS in operation:

![MAVIS example](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/mavis-1-5-demo-3.png)

![MAVIS example](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/mavis-1-5-demo-4.png)

![MAVIS example](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/mavis-1-5-demo-5.png)

By default, the formula editor is open, which you can use to draw formulas. The drawn formulas are converted to LaTeX code in the input box below and displayed correctly rendered directly below. To convert the formula, simply press the black play button in the drawing box.

The input box in which the LaTeX code is written is connected to the lower input box in the taskbar and can be used as input for the AI-Chatbot.

![Formula editor use](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/mavis-1-5-use-gif-1.gif)

To close the formula editor, press the pen button in the main taskbar.

![Formula editor usage](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/mavis-1-5-use-gif-2.gif)

You can also use the graph editor to display formulas in a 2D or 3D coordinate system.

![Graph editor](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/using-img-4.png)

Enter your formula and use the "Select" function to select special characters, pre-defined formulas, operations (derivation and integration) and the display as a 2D or 3D diagram (2D by default). The formula is displayed in real time.

![Formula display](https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/using-img-5.png)

You can close this window at any time by clicking on the corresponding icon in the taskbar again.

<div align="center">
<img src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/using-img-6.png" alt="pen-button" width="600">
</div>

Have fun with MAVIS! Over time, you will get used to using the chatbot. Always give the chatbot a clear role, e.g.: "You are a professional programmer and your job is [...] - get to work!"
