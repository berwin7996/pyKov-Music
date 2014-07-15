#pyKov-Music



###References used: 
- http://www.fourmilab.ch/webtools/midicsv/
- https://github.com/SIGMusic/osc-example

###What you will need (from https://github.com/SIGMusic/osc-example):

  - PureData Extended
  - Python - http://www.python.org/getit/
    - pyOSC - https://trac.v2.nl/wiki/pyOSC
    - simpleOSC - http://ixi-audio.net/content/download/SimpleOSC_0.3.2.zip

###Installation Instructions:

#####pyOSC and simpleOSC

  1.  Open command prompt and confirm Python is installed correctly by typing:
  
          python --version
    
      You should see the version number of your python installation appear.
    
  2.  Extract the pyOSC archive
  3.  Change the active directory of the command prompt to the directory of the extracted files. In Windows, this is:

          cd c:\Users\user\downloads\pyOSC-directory
  4.  Type in the following command:

          python setup.py install
          
  5.  Repeat steps 2-4 with the simpleOSC archive

###Making it run
Take your .mid file and run it through the 'midicsv' program.  NOTE: try to find midi files of format 0, because those come in single channels which make it easier to parse

    ./midicsv [input-file] [output-file]
  
With that output, run it through the 'midi_csv_to_txt.py' program by doing

    python midi_csv_to_txt.py [csv-file]
    

Once those have run, open up your PureData synth of choice, I've included one from SIGMusic tutorials named 'osctoot.pd'
  Make sure DSP is checked!
After all of that is set, it's time to run the probabilistic compositor!
  
    python p_music.py [txt-file]
    
the txt file is of all of the midi notes, and now it should be outputing 'music'!
