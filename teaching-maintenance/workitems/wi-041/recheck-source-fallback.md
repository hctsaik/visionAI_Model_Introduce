# External source reachability fallback — 2026-09-13

The initial scan treated source-prose fields as single URLs. Fourteen failed entries contain multiple links or section notes, so those are audit extraction failures, not fourteen broken website links. `recheck-source-links.py` extracts individual URLs and uses GET for the corrected evidence.

Local urllib returned HTTP 403 on eleven OpenCV URL forms and a certificate-chain error on the ECVA PDF. The web browsing tool successfully read the following exact resources (including redirects on 4.x) in this review. This confirms resource availability through another client; it does not establish universal reachability or bypass TLS validation in the product.

- https://docs.opencv.org/4.13.0/d1/dc5/tutorial_background_subtraction.html
- https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html
- https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html
- https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
- https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
- https://docs.opencv.org/4.x/d1/dc5/tutorial_background_subtraction.html
- https://docs.opencv.org/4.x/d2/de8/group__core__array.html
- https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html
- https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html
- https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
- https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123470392.pdf (17-page PDF)

These access errors do not justify replacing official citations or classifying the website as broken. Actual rendered href validity is a separate browser audit item.
