# SRI-Test
Subresource Integrity Testing

# Prerequisites 
   - Python 3+
   - A web browser

# To Run

    python -m http.server

- Open sri_test_good.html to see how SRI validation checks out.

- Open sri_test_bad.html to see SRI validation fail. *Check your browser console* for the error message.

# Generating integrity values

From a terminal call `sri_gen.py` with your file name as:
    ./sri_gen.py -i your_file.js

Place the resulting string in an `integrity` element like so

`<script src="your_file.js" crossorigin="anonymous" integrity="sha384-BLAH.BLAH="/>`

Please note the `crossorigin="anonymous"` is required as per the [W3C](https://w3c.github.io/webappsec-subresource-integrity/#cross-origin-data-leakage)
