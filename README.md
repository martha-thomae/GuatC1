# Experiment Dataset from GuatC 1
This branch contains the dataset for the experiment evaluating whether the use of a dissonance labeller in the initial score provided by the [Measuring Polyphony (MP) Editor](https://editor.measuringpolyphony.org/#/) does affect the efficiency of the correction process. At this point, most of the corrections are editorial in nature since corrections for symbol recogntion (and pitch) have already been done in the OMR step through [MuRET](https://muret.dlsi.ua.es/muret/#/). This dataset consists of a random selection of fifteen pieces from the Guatemalan Cathedral Choirbook 1 (GuatC 1), where each piece was either a mass movement or a short polyphonic piece. The fifteen pieces represent around 20% of the total corpus. To ease the editorial work in the MP Editor, the long mass movements were subdivided into smaller units called “self-contained units.” Here, “long movement” is considered as a movement that occupies more than two openings (i.e., four pages) in the manuscript. And a “self-contained unit” is defined as the minimum number of consecutive sections (one or more) that start at a page beginning and end at a page ending. This definition was needed because we had to face the problem of handling sections whose beginning or end do not correspond to the beginning or ending of an image (i.e., a page) since MuRET can only produce an MEI output from a set of one or more selected images.

This division of the long movements resulted in a total of 23 self-contained units, which were divided into two datasets: a DF Dataset where the dissonance filter would be activated during the correction process, and a NDF Dataset where no dissonance filter would be used during correction. To guarantee a balanced dataset, the pieces were arranged so that the DF and NDF datasets have the same average number of measures, voices, and illegal dissonances. We also made sure that each dataset had close to the same number of CPDL transcriptions to use as a reference, providing another musician’s interpretation of where the mistakes are found and how to fix them. The two datasets are shown in the tables below.

#### NDF Dataset
<img width="872" alt="dataset_ndf" src="https://user-images.githubusercontent.com/13948831/194136283-de9fa806-831a-4276-9b7d-08e02a43b3d3.png">

#### DF Dataset
<img width="870" alt="dataset_df" src="https://user-images.githubusercontent.com/13948831/194136302-ecaa2cff-9d49-44d7-a230-c71b9b882134.png">


## Results

The observations for each piece are summarized in [Appendix C](Appendix%20C.pdf). The correction time can be seen in the following tables.

#### NDF Correction Time Results
<img width="1333" alt="results_ndf" src="https://user-images.githubusercontent.com/13948831/194136341-aa9b79ef-16e2-4068-8f36-5c1d4ec29af8.png">

#### DF Correction Time Results
<img width="1333" alt="results_df" src="https://user-images.githubusercontent.com/13948831/194136367-3e8dd945-395a-4605-9d2b-50a49c09031b.png">
