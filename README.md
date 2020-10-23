# SRI-Test
Subresource Integrity Testing

# Prerequisites 
   - Python 3+
   - A web browser

# To Run

    python -m http.serverr

- Open sri_test_good.html to see how SRI validation checks out.

- Open sri_test_bad.html to see SRI validation fail. *Check your browser console* for the error message.

# Generating integrity values

In `srgen.py` you can just edit the `with open('sri_test.js', 'rb') as f:` line replacing `sri_test.js` with your file name.

Then in a console execute `python sri_gen.py` and plave the resulting string an `integrity` element like so

`<script src="your_file.js" crossorigin="anonymous" integrity="sha384-BLAH.BLAH="/>`

Please note the `crossorigin="anonymous"` is required as per the [W3C](https://w3c.github.io/webappsec-subresource-integrity/#cross-origin-data-leakage)
