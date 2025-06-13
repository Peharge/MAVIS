# Using MAVIS 1.5

## 1. Starting the MAVIS Installer
After you have run the appropriate `.bat` or `.sh` file for the desired MAVIS version, a terminal will open on your operating system. This is the MAVIS Installer.

If you are starting MAVIS 1.5 for the first time, the installation can take between 30 minutes and 2 hours, depending on your internet speed. If MAVIS is already installed, the program will start in about a minute.

Regardless of the state of the installation, the system is always checked for completeness and updated if necessary.

## 2. Installing the required frameworks
Once the terminal is opened, a list of Python frameworks required for MAVIS will appear. These frameworks allow MAVIS to perform various tasks. You can also use them later in Jupyter Notebook, as MAVIS runs in its own Python environment.

For example, the output might look like this:

```bash
Framework Information:
----------------------
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

![MAVIS](../readme-img/using-img-1.png)

## 6. Using MAVIS
You can now send questions to the chatbot, upload images and use the control panel.

![Using MAVIS](../readme-img/using-img-2.png)

Once you have uploaded an image, a small window will appear with the image. Simply click on the window to close it.

If you want to ask the chatbot to create a graph, tell it to use one of the following frameworks:
- Matplotlib
- Plotly
- Seaborn
- Altair

MAVIS also supports LaTeX for mathematical formulas and can perform calculations directly.

Here is an example of MAVIS in operation:

![MAVIS example](../readme-img/mavis-1-5-demo-3.png)

![MAVIS example](../readme-img/mavis-1-5-demo-4.png)

![MAVIS example](../readme-img/mavis-1-5-demo-5.png)

By default, the formula editor is open, which you can use to draw formulas. The drawn formulas are converted to LaTeX code in the input box below and displayed correctly rendered directly below. To convert the formula, simply press the black play button in the drawing box.

The input box in which the LaTeX code is written is connected to the lower input box in the taskbar and can be used as input for the AI-Chatbot.

![Formula editor use](../readme-img/mavis-1-5-use-gif-1.gif)

To close the formula editor, press the pen button in the main taskbar.

![Formula editor usage](../readme-img/mavis-1-5-use-gif-2.gif)

You can also use the graph editor to display formulas in a 2D or 3D coordinate system.

![Graph editor](../readme-img/using-img-4.png)

Enter your formula and use the "Select" function to select special characters, pre-defined formulas, operations (derivation and integration) and the display as a 2D or 3D diagram (2D by default). The formula is displayed in real time.

![Formula display](../readme-img/using-img-5.png)

You can close this window at any time by clicking on the corresponding icon in the taskbar again.

<div align="center">
<img src="../readme-img/using-img-6.png" alt="pen-button" width="600">
</div>

Have fun with MAVIS! Over time, you will get used to using the chatbot. Always give the chatbot a clear role, e.g.: "You are a professional programmer and your job is [...] - get to work!"