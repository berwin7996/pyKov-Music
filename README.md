pyKov-Music



References used: http://www.fourmilab.ch/webtools/midicsv/

In order to make this run:
Take your .mid file and run it through the 'midicsv' program.  NOTE: try to find midi files of format 0, because those come in single channels which make it easier to parse

    ./midicsv [input-file] [output-file]
  
With that output, run it through the 'midi_csv_to_txt.py' program by doing

    python midi_csv_to_txt.py [csv-file]
    

Once those have run, open up your PureData synth of choice, I've included one from SIGMusic tutorials named 'osctoot.pd'
  Make sure DSP is checked!
After all of that is set, it's time to run the probabilistic compositor!
  
    python p_music.py [txt-file]
    
the txt file is of all of the midi notes, and now it should be outputing 'music'!
