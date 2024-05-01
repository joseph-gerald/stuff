# Download all images from a facebook photo album
Simple method to get all the images from a facebook photo album

1. Find download css path
    1. Click the 3 dots on an image and use dev tools to copy the css path

2. Open download menu on all images
    1. Find css selector
    2. Replace the first child selector with `${i}`
    3. ```css
        div.x1vtvx1t:nth-child(${i}) > a:nth-child(1) > div:nth-child(3) > div:nth-child(1)
    4. ```js
        for (let i = 1; i < 10000; i++) document.querySelector(`YOUR_TEMPLATE_LITERAL`)
    5. Run the javascript in browser

3. Collect all download URLs/paths
    1. Use css path from earlier
    2. ```js
        JSON.stringify([...document.querySelectorAll("YOUR_PATH")].map(elm => elm.href))
    3. Run in js in browser
    3. Save the JSON into `images.json`

4. Download all the images into a directory
    1. Create a `/images` directory
    2. Run `main.py`
    3. Wait (create a pull req with concurrency please, i was too lazy and didn't need it)
    4. Enjoy your images