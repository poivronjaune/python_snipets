# THINGINO 
[Thingino](https://thingino.com/) is an open source project to overrite the firmware of many webcam devices to remove the cloud connection requirememnts.  

An RTSP (Real Time Streaming Protocol) is offered on this firmware. We will connect to it to display and save images.  


---

# Installing FFmpeg on Windows 11 (Step-by-Step)

This guide explains how to install **FFmpeg** on a Windows 11 (or newer) PC so it can be used **from anywhere**, including Python scripts, PowerShell, and Command Prompt. Connecting to a reprogrammed webcamera using [Thingino](https://thingino.com/) open source software.  

---

## 1️⃣ Download FFmpeg (important: choose the right build)

### Why gyan.dev?

FFmpeg does **not** provide official Windows binaries itself.
Instead, trusted third-party builders compile FFmpeg for Windows.

**gyan.dev** is one of the most widely used and trusted sources because:

* Builds are **up-to-date**
* Includes **all major codecs** (H.264, H.265, RTSP, etc.)
* Provides **static builds** (no extra DLLs needed)

### Steps

1. Go to **[https://www.ffmpeg.org](https://www.ffmpeg.org)**
2. Click **Download**
3. Click **Windows**
4. Choose **Windows builds by gyan.dev**
5. Download a file named similar to:

   ```
   ffmpeg-*-win64-static.zip
   ```

✅ **Important:**
Choose a **static** build.
Static builds include everything in one executable and are easiest to use.

---

## 2️⃣ Extract `ffmpeg.exe` from the ZIP file

1. Right-click the downloaded ZIP file
2. Select **Extract All**
3. Open the extracted folder

Inside, you will typically find:

```
ffmpeg.exe
ffprobe.exe
ffplay.exe
```

For basic usage, **`ffmpeg.exe` is the only required file**.

---

## 3️⃣ Copy `ffmpeg.exe` to `C:\ffmpeg\bin`

Windows searches for executables using the **PATH environment variable**.
Placing FFmpeg in a dedicated `bin` folder follows standard conventions and makes it easy to manage later.

### Steps

1. Create the following folder:

   ```
   C:\ffmpeg\bin
   ```
2. Copy **`ffmpeg.exe`** into:

   ```
   C:\ffmpeg\bin\ffmpeg.exe
   ```

### Why the `bin` folder is important

* Required for using "ffmpeg -version" from command line
* Keeps executables organized
* Makes PATH configuration clean
* Avoids cluttering system folders
* Matches how most developer tools are installed

---

## 4️⃣ Add FFmpeg to the PATH environment variable

This allows you to run `ffmpeg` from **any folder**.

### Steps

1. Press **Win + R**
2. Type:

   ```
   sysdm.cpl
   ```

   and press Enter
3. Go to the **Advanced** tab
4. Click **Environment Variables**
5. Under **System variables**, select **Path**
6. Click **Edit**
7. Click **New**
8. Add:

   ```
   C:\ffmpeg\bin
   ```
9. Click **OK** → **OK**

⚠️ **Important**

* Add the **folder**, not `ffmpeg.exe`
* You must restart PowerShell or Command Prompt for changes to apply

---

## 5️⃣ Verify the installation in PowerShell

### Open a new PowerShell window

Close all existing PowerShell windows and open a new one.

### Run:

```powershell
ffmpeg -version
```

### Expected result

You should see output similar to:

```
ffmpeg version ...
built with gcc ...
libavcodec ...
libavformat ...
```

If you see version information, **FFmpeg is installed correctly**.

