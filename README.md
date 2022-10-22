# SWR Nomograph for Drake W-4 power meter

This just contains a short python code using the PyNomo package to
more or less reproduce the Drake nomograph to compute the SWR given
the forward and reverse power readings. I added a return loss scale.
The mathematics needed is the swrnomograph.tex file. The python
code is in w4_swr.py. The produced nomograph is in w4_swr_nomograph.pdf.

If you wish to modify the nomograph, then use any method equivalent to
- Install python
- pip install -r requirements.txt
- python w4_swr.py
