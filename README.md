# lang-fixer

A python script that fixes typing in the wrong language when you tap a (configurable) hotkey.

## Installation

### Prerequisites

You need to have the following software installed on your machine:

1. Python (3)
1. pipenv - manages a python script's dependencies inside a venv for you, so the dependencies are not installed in your global scope.  
   Install pipenv by running:
   ```shell
   pip install pipenv
   ```

### Installing lang-fixer

1. Clone this repository:

   ```shell
   git clone https://github.com/TheYarin/lang-fixer.git
   ```

1. run:
   ```shell
   cd lang-fixer
   pipenv install
   ```

## Running lang-fixer

If you're using Windows, you can simply run the `run.bat` file.

Otherwise, run:

```shell
cd lang-fixer
pipenv run python ./lang-fixer.py
```

## How to use the fixer

When you've made the typo, hit the `pause` button (usually found above the `Page Up` button).

## Changing Settings

You can change the hotkey that triggers the fixing in the `settings.json` file. You can use a syntax like `ctrl+shift+a`.

In general, these are the configurable settings in `settings.json`:

```json
{
  "TRIGGER_HOTKEY": "pause",
  "OS_SPECIFIC": {
    "WINDOWS": {
      "COPY": "ctrl+c",
      "CHANGE_LANGUAGE": "alt+shift"
    },

    "LINUX": {
      "COPY": "ctrl+c",
      "CHANGE_LANGUAGE": "alt+shift"
    },

    "MAC_OS": {
      "COPY": "cmd+c",
      "CHANGE_LANGUAGE": "ctrl+space"
    }
  }
}
```

## Known issues

This tool uses the clipboard to get the text you typed, and while it attempts to restore any previous value that was in the clipboard before overriding it, the restoration only works if the previous value is textual. It's recommended to use a clipboard manager to avoid losing important clipboard content.
