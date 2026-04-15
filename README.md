# Screenlock Preventer

A lightweight Python utility designed to keep your computer active and prevent the screen from locking or the system from going into sleep mode during periods of inactivity.

## How It Works

The script monitors your system for activity. If no mouse movement or keyboard input is detected for a predefined interval (default is 60 seconds), the application performs a "ghost" action:
1. It momentarily moves the mouse to the top-left corner (0,0).
2. It performs a single left-click.
3. It instantly returns the mouse cursor to its original position.

This effectively simulates user activity to the operating system without interrupting your workflow.

## Features

- **Activity Detection**: Only triggers if you are truly idle; it resets its timer every time you move the mouse or press a key.
- **Batch Startup**: Includes a `start.bat` file for quick, one-click execution on Windows.
- **Low Overhead**: Runs quietly in the background with minimal CPU usage.

## Prerequisites

Before running the application, ensure you have Python installed.