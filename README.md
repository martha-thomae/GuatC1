# GuatC1
This repository contains the scores of each of the works contained in the first polyphonic choirbook used in Guatemala's Metropolitan Catheral in colonial times. This manuscript has been known by the sigla:
- **GuatC 1**, according to the Census Catalogue
- **GCA-Gc 1**, according to the [Digital Image Archive of Medieval Music (DIAMM)](https://www.diamm.ac.uk/sources/985/)
- **GCA-Gaha 1**, would be its correct siglum given its current location at the Archivo Histórico Arquidiocesano "Francisco de Paula García Peláez", Ciudad de Guatemala (GCA-Gaha) (see [RISM](https://rism.online/search?q=guatemala&mode=institutions&page=1&rows=40#institutions-30080989))

This manuscript is a book of Masses, containing 12 masses (six copied from a book written by Gaspar Fernández in 1602 and six newly added by Manuel José de Quirós) and 15 short polyphonic pieces. Each of the individual folders contain the MEI files encoding the scores for each movement of the masses, or each section of the short polyphonic pieces.

Opening the MEI scores in [mei-friend](https://mei-friend.mdw.ac.at) (please, open it in Chrome or Firefox, not Safari) would allow to:
1. Visualize the transcribed score
2. Visualize the images of the original source containing this work
3. Play back the music (in midi keyboard)
4. See and edit the MEI encoding

<img width="2560" height="1331" alt="Screenshot 2026-01-04 at 11 56 03 PM" src="https://github.com/user-attachments/assets/f6b87f5d-454b-4d09-a645-1010b6d8e4f5" />

----

You can try it yourself! For example, you can go to the file [`06_Cristobal-de-Morales_Mass/Missa6.1_Kyrie_FullMovement_f17v-19r_MensuralScore-and-Facsimile.xml`](06_Cristobal-de-Morales_Mass/Missa6.1_Kyrie_FullMovement_f17v-19r_MensuralScore-and-Facsimile.xml), download the file (see screenshot), and then load it into [mei-friend](https://mei-friend.mdw.ac.at) by going into the _File_ menu and click on _Open file_.

<img width="1260" height="1248" alt="Screenshot 2026-01-04 at 11 53 14 PM" src="https://github.com/user-attachments/assets/97d24974-2b38-41ac-a47e-768ca0be02f7" width="100"/>

----

## How were these scores obtained?

The scores were obtained by performing OMR using MuRET and then scoring up the mensural voices using the Measuring Polyphony (MP) Editor. If you want to consult the results obtained by MuRET and by the MP Editor, please check the branch [`all_data_omr_and_mped`](https://github.com/martha-thomae/GuatC1/tree/all_data_omr_and_mped).
