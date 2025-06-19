# Anniversary

This repository contains a small static website found in the `site/` folder.
The site celebrates an anniversary and requires an access code to view the
content beyond the landing page.

## Usage

Open `site/index.html` in your web browser. Enter the access code `0425`
when prompted to read the anniversary letter and view the photo slideshow.

You can also serve the files locally with Python:

```bash
cd site
python3 -m http.server 8000
```

Then visit [http://localhost:8000](http://localhost:8000) in your browser.
