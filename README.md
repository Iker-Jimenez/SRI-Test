# SRI-Test
Subresource Integrity Testing

# Prerequisites 
   - Python 2.7+
   - A web browser

# To Run

    python -m SimpleHTTPServer

Simply edit the `sri_test.js` file to cause an integrity validation error.

# Generating integrity values

In `srgen.py` you can just edit the `with open('sri_test.js', 'rb') as f:` line replacing `sri_test.js` with your file name.

Then in a console execute `python srgen.py` and plave the resulting string an `integrity` element like so

`<script src="your_file.js" crossorigin="anonymous" integrity="sha256-BLAH.BLAH="/>`

Please note the `crossorigin="anonymous"` is required as per the [W3C](https://w3c.github.io/webappsec-subresource-integrity/#cross-origin-data-leakage)
