# Test automation for our TODO list app
Automation! For when you want to make sure no random thing got broken by a new feature but you just don't have the time to do all those blasted basic tests!

## Requirements
- Node.js (can be installed via [homebrew](https://brew.sh/) or on the [official website](https://nodejs.org/en/))

## How to get this going

### Step 1
Install Node.js (see above)

### Step 2
In your terminal, from the root directory (a directory above this one), run the following:
```
npm install
```
(Note: npm will only exist if you've successfully installed node.js)


### Step 3
Run your test!

To run a quick, headless (read: browser window not visible) run, use the following command:
```
npm run test
```

If you want a GUI that breaks everything down for you and looks snazzy, use the following command:
```
npm run cypress:open
```