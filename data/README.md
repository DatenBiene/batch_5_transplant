# Data Directory
## Sommaire
- <a href="#dataset">**Dataset**</a>
- <a href="#usage">**Usage**</a>
- <a href="#documentation">**Documentation des variables**</a>


<div id="dataset">

## Dataset

Le dataset contient les données relatives à 411 transplantations pulmonaires ayant été réalisées par les équipes de l'hôpital Foch depuis Janvier 2012.
Elles sont issues de la collecte manuelle d'information de la part des équipes médicales, ou de l'export automatique d'instruments de mesure lors de l'opération.


Les données ont été divisées en deux principales catégories :
- **Variables Statiques** : elles représentent les données charactéristiques du patient et de son donneur. Ces variables sont "figées" dans le temps, la table `clean/static.csv` correspondante contient donc une seule ligne pour chacun des 411 patients.
- **Variables Dynamiques** : elles représentent les mesures prises *chaque minute* par les instruments de mesure lors de l'opération. Elles sont évolutives dans le temps, la table `clean/dynamic.csv` correspondante contient donc plusieurs lignes par patient, chacune identifiée par un timestamp.

Pour plus de clarté, ces données ont été subdivisées en plusieurs catégories. Elle sont décrites dans la <a href="#documentation">documentation</a> en annexe.
Les catégories sont les suivantes :
- <a href="#static_variables">**Variables Statiques**</a>
    - <a href="#patient_preoperative">Patient Preoperative</a>
    - <a href="#patient_intraoperative">Patient Intraoperative</a>
    - <a href="#patient_postoperative">Patient Postoperative</a>
    - <a href="#donor">Donor</a>
    - <a href="#target">Target variable</a>
- <a href="#dynamic_variables">**Variables Dynamiques**</a>
    - <a href="#haemodynamic">Haemodynamic</a>
    - <a href="#respiratory">Respiratory</a>
    - <a href="#neurology">Neurology</a>
    - <a href="#temperature">Temperature</a>

</div>
<div id="usage">

## Usage
#### Organisation du dossier data
- **clean** : dossier contenant les `.csv` des variables statiques et dynamiques nettoyées.
- **raw** : dossier contenant les données brutes (raw).

#### Pour générer les clean à partir des données brutes
```
python transplant/data/build_clean_from_raw_data.py
```

#### Pour importer les données statiques et dynamiques
```
from transplant.config import PATH_STATIC_CLEAN, PATH_DYNAMIC_CLEAN

df_static = pd.read_csv(PATH_STATIC_CLEAN)
df_dynamic = pd.read_csv(PATH_DYNAMIC_CLEAN)
```

#### Pour filtrer par sous catégories
Par exemple pour filtrer les données respiratoires dans les données dynamiques :
```
from transplant.config import PATH_DYNAMIC_CLEAN, DYNAMIC_CATEGORIES

df_dynamic = pd.read_csv(PATH_DYNAMIC_CLEAN)
df_respiratory = df_dynamic[DYNAMIC_CATEGORIES['respiratory']]
```

</div>
<div id="documentation">

## Documentation des variables

<div id="static_variables">

### Variables Statiques
Le fichier `clean/static.csv` contient des données charactéristiques du patient et de son donneur.
Cette table contient une seule ligne pour chacun des 411 patients.

Les patients sont identifiés par la colonne `id_patient`, ce qui permet de joindre les tables entre elles.
Les autres colonnes peuvent être subdivisées en 4 catégories :
- <a href="#patient_preoperative">Patient Preoperative</a> : données charactéristiques du patient avant que l'opération ait été réalisée
- <a href="#patient_intraoperative">Patient Intraoperative</a> : données intra-opératoire du patient, référençant les mesures et notes prises lors de l'opération à chaque étape clé (clampage, déclampage).
- <a href="#patient_postoperative">Patient Postoperative</a> : données charactéristiques du patient après que l'opération ait été réalisée
- <a href="#donor">Donor</a> : données du donneur d'organe


Ces dernières sont détaillées dans les sections qui suivent.


<div id="patient_preoperative">

#### Patient Preoperative
|	Colonne	|	Unité	|	Description	|	Etendue	|	Normalité	|
|	----	|	----	|	----	|	----	|	----	|
|	date_transplantation	|	date	|	date à laquelle a lieu la transplantation	|		|		|
|	heure_arrivee_bloc	|	HH:MM:SS |	heure d'arrivée au bloc	|		|		|
|	pathologie	|	Int	|	Pathologie du patient. muco = 1 , emphyseme/BPCO = 2 , fibroses = 3 , GVH = 4 , DDB = 5 , BOOP/BOS3 = 6 , autres = 7 , ATTENTION, on peut faire une catégorie 9 = 4+5+6+7	|		|		|
|	age	|	Int	|	continu	|		|		|
|	sexe	|	Int	|	Sexe du patient. homme = 1 , femme = 0	|		|		|
|	Poids	|	Int	|	Poids du patient.	|		|		|
|	Taille	|	Int (en cm)	|	Taille du patient	|		|		|
|	other_organ_transplantation	|	Int	|	Le patient a subi d'autres transplantations 0 = uniquement poumon ; foie = 1 ; rein = 2	|		|		|
|	super_urgence 	|	Bool	|	Le patient a été admis en super-urgence. oui = 1 , non = 0	|		|		|
|	retransplant	|	Bool	|	Il s'agit d'une re-transplantation. oui = 1 , non = 0	|		|		|
|	transplanted_twice_during_study_period	|		|	oui = 1 , non = 0	|		|		|
|	time_on_waiting_liste	|	Int	|	Durée d'attente sur la liste d'attente avant d'avoir subi une transplantation (en nombre de jours)	|		|		|
|	LAS	|		|	continu	|		|		|
|	preoperative_ICU	|		|	oui = 1 , non = 0	|		|		|
|	preoperative_vasopressor	|		|	oui = 1 , non = 0	|		|		|
|	preoperative_mechanical_ventilation	|		|	oui = 1 , non = 0	|		|		|
|	ATCD_medicaux	|		|	text	|		|		|
|	PFO	|		|	oui = 1 , non = 0	|		|		|
|	body_mass_index	|		|	index	|		|		|
|	diabetes	|	Bool	|	Le patient est atteint de diabète. oui = 1 , non = 0	|		|		|
|	preoperative_pulmonary_hypertension	|		|	oui = 1 , non = 0	|		|		|
|	PAPS	|		|	continu	|		|		|
|	Insuffisance_renale	|	Bool	|	oui = 1 , non = 0	|		|		|
|	CMV_receveur	|		|	positif ou negatif	|		|		|
|	plasmapherese	|		|	positif ou negatif	|		|		|
|	preoperative_ECMO	|		|	oui = 1 , non = 0	|		|		|
|	ATCD_chirugicaux	|		|	text	|		|		|
|	thoracic_surgery_history	|		|	oui = 1 , non = 0	|		|		|

</div>
<div id="patient_intraoperative">

#### Patient Intraoperative
|	Colonne	|	Unité	|	Description	|	Etendue	|	Normalité	|
|	----	|	----	|	----	|	----	|	----	|
|	exvivo	|		|	oui = 1 , non = 0	|		|		|
|	Immunosuppresseurs	|		|	text	|		|		|
|	heure_transfert_rea	|		|	heure	|		|		|
|	date_sortie_bloc	|		|	date	|		|		|
|	duree_sejour_bloc	|		|	continu	|		|		|
|	Antibioprophylaxie	|		|	text	|		|		|
|	PB_induction	|		|	oui = 1 , non = 0	|		|		|
|	Pb_induction_detail	|		|	text	|		|		|
|	FIO2_initiale	|		|	continu	|		|		|
|	pH_initial	|		|	continu	|		|		|
|	PAPS_initiale	|		|	continu	|		|		|
|	PA_initiale	|		|	continu	|		|		|
|	VT_initial	|		|	continu	|		|		|
|	PaCO2_initial	|		|	continu	|		|		|
|	PAPM_initiale	|		|	continu	|		|		|
|	Fc_initiale	|		|	continu	|		|		|
|	FR_initial	|		|	continu	|		|		|
|	PaO2_initial	|		|	continu	|		|		|
|	PAPD_initiale	|		|	continu	|		|		|
|	NORAD_initiale	|		|	continu	|		|		|
|	PEEP_initial	|		|	continu	|		|		|
|	Bicarbonates_initial	|		|	continu	|		|		|
|	NO_initiale	|		|	oui = 1 , non = 0	|		|		|
|	Lactate_initial	|		|	continu	|		|		|
|	SvO2_initiale	|		|	continu	|		|		|
|	Ic_initial	|		|	continu	|		|		|
|	Hb_initial	|		|	continu	|		|		|
|	Qc_initiale	|		|	continu	|		|		|
|	Examen_Echographique_initial	|		|	text	|		|		|
|	Problemes_VBP	|		|	oui = 1 , non = 0	|		|		|
|	Problemes_VBP_commentaires	|		|	text	|		|		|
|	premiere_transplantation_cote	|		|	DROIT ou GAUCHE	|		|		|
|	Ventilation_Unipulmonaire_Pb	|		|	text	|		|		|
|	FiO2_clampage_cote_1	|		|	continu	|		|		|
|	PH_clampage_cote_1	|		|	continu	|		|		|
|	PAPS_clampage_cote_1	|		|	continu	|		|		|
|	PA_clampage_cote_1	|		|	continu	|		|		|
|	VT_clampage_cote_1	|		|	continu	|		|		|
|	PaCO2_clampage_cote_1	|		|	continu	|		|		|
|	PAPM_clampage_cote_1	|		|	continu	|		|		|
|	FC_clampage_cote_1	|		|	continu	|		|		|
|	Fr_clampage_cote_1	|		|	continu	|		|		|
|	PaO2_clampage_cote_1	|		|	continu	|		|		|
|	PAPD_clampage_cote_1	|		|	continu	|		|		|
|	NORAD_clampage_cote_1	|		|	continu	|		|		|
|	PEEP_clampage_cote_1	|		|	continu	|		|		|
|	Bicarbonates_clampage_cote_1	|		|	continu	|		|		|
|	NO_clampage_cote_1	|		|	oui = 1 , non = 0	|		|		|
|	Evolution_PAP_clampage_cote_1	|		|	diminution ou augmentation	|		|		|
|	Lactates_clampage_cote_1	|		|	continu	|		|		|
|	SvO2_clampage_cote_1	|		|	continu	|		|		|
|	Ic_clampage_cote_1	|		|	continu	|		|		|
|	Hb_clampage_cote_1	|		|	continu	|		|		|
|	Qc_clampage_cote_1	|		|	continu	|		|		|
|	Examen_Echographique_clampage_cote_1	|		|	text	|		|		|
|	evenements_clampage_cote_1	|		|	oui = 1 , non = 0	|		|		|
|	evenements_clampage_cote_1_commentaires	|		|	text	|		|		|
|	Heure_declampage_cote1	|		|	heure	|		|		|
|	first_lung_ischemic_time	|		|	continu	|		|		|
|	FiO2_declampage_cote1	|		|	continu	|		|		|
|	PH_declampage_cote_1	|		|	continu	|		|		|
|	PAPS_declampage_cote_1	|		|	continu	|		|		|
|	PA _declampage_cote_1	|		|	continu	|		|		|
|	VT_declampage_cote_1	|		|	continu	|		|		|
|	PaCO2_declampage_cote_1	|		|	continu	|		|		|
|	PAPM_declampage_cote_1	|		|	continu	|		|		|
|	FC_declampage_cote_1	|		|	continu	|		|		|
|	Fr_declampage_cote_1	|		|	continu	|		|		|
|	PaO2_declampage_cote_1	|		|	continu	|		|		|
|	PAPD_declampage_cote_1	|		|	continu	|		|		|
|	NORAD_declampage_cote_1	|		|	continu	|		|		|
|	PEEP_declampage_cote_1	|		|	continu	|		|		|
|	Bicarbonates_declampage_cote_1	|		|	continu	|		|		|
|	NO_declampage_cote_1	|		|	oui = 1 , non = 0	|		|		|
|	Evolution_PAP_declampage_cote_1	|		|	diminution ou augmentation ou stabilité	|		|		|
|	SvO2_declampage_cote_1	|		|	continu	|		|		|
|	Lactates_declampage_cote_1	|		|	continu	|		|		|
|	Ic_declampage_cote_1	|		|	continu	|		|		|
|	Hb_declampage_cote_1	|		|	continu	|		|		|
|	Qc_declampage_cote_1	|		|	continu	|		|		|
|	Examen_Echographique_declampage_cote_1	|		|	text	|		|		|
|	evenements_declampage_cote_1	|		|	oui = 1 , non = 0	|		|		|
|	evenements_declampage_cote_1_commentaires	|		|	text	|		|		|
|	Saigement_estime_declampage_cote1	|		|	continu	|		|		|
|	classification_bullage_1	|		|	 0 = pas de bulles, 1 = Bullage minime, 2 = bullage modéré,  3 = bullage majeur	|		|		|
|	duree_bullage_1	|		|	< 20 sec ; 20 à 60 sec ; 1 à 3 min ; > 3 min	|		|		|
|	retentissement_ETO_bullage_1	|		|	oui = 1 , non = 0	|		|		|
|	retentissement_ECG_bullage_1	|		|	oui = 1 , non = 0	|		|		|
|	retentissement_BIS_bullage_1	|		|	oui = 1 , non = 0	|		|		|
|	Retentissement_hemodynamique_bullage_1	|		|	oui = 1 , non = 0	|		|		|
|	deuxieme_transplantation_cote	|		|	DROIT ou GAUCHE	|		|		|
|	Ventilation_Unipulmonaire_Pb.1	|		|	text	|		|		|
|	FiO2_clampage_cote_2	|		|	continu	|		|		|
|	PH_clampage_cote_2	|		|	continu	|		|		|
|	PAPS_clampage_cote_2	|		|	continu	|		|		|
|	PA_clampage_cote_2	|		|	continu	|		|		|
|	VT_clampage_cote_2	|		|	continu	|		|		|
|	PaCO2_clampage_cote_2	|		|	continu	|		|		|
|	PAPM_clampage_cote_2	|		|	continu	|		|		|
|	FC_clampage_cote_2	|		|	continu	|		|		|
|	Fr_clampage_cote_2	|		|	continu	|		|		|
|	PaO2_clampage_cote_2	|		|	continu	|		|		|
|	PAPD_clampage_cote_2	|		|	continu	|		|		|
|	NORAD_clampage_cote_2	|		|	continu	|		|		|
|	PEEP_clampage_cote_2	|		|	continu	|		|		|
|	Bicarbonates_clampage_cote_2	|		|	continu	|		|		|
|	NO_clampage_cote_2	|		|	oui = 1 , non = 0	|		|		|
|	Evolution_PAP_clampage_cote_2	|		|	diminution ou augmentation ou stabilité	|		|		|
|	Lactates_clampage_cote_2	|		|	continu	|		|		|
|	SvO2_clampage_cote_2	|		|	continu	|		|		|
|	Ic_clampage_cote_2	|		|	continu	|		|		|
|	Hb_clampage_cote_2	|		|	continu	|		|		|
|	Qc_clampage_cote_2	|		|	continu	|		|		|
|	Examen_Echographique_clampage_cote_2	|		|	text	|		|		|
|	evenements_clampage_cote_2	|		|	oui = 1 , non = 0	|		|		|
|	evenements_clampage_cote_2_commentaires	|		|	text	|		|		|
|	Heure_declampage_cote2	|		|	heure	|		|		|
|	second_lung_ischemic_time	|		|	continu	|		|		|
|	FiO2_declampage_cote2	|		|	continu	|		|		|
|	PH_declampage_cote_2	|		|	continu	|		|		|
|	PAPS_declampage_cote_2	|		|	continu	|		|		|
|	PA _declampage_cote_2	|		|	continu	|		|		|
|	VT_declampage_cote_2	|		|	continu	|		|		|
|	PaCO2_declampage_cote_2	|		|	continu	|		|		|
|	PAPM_declampage_cote_2	|		|	continu	|		|		|
|	FC_declampage_cote_2	|		|	continu	|		|		|
|	Fr_declampage_cote_2	|		|	continu	|		|		|
|	PaO2_declampage_cote_2	|		|	continu	|		|		|
|	PAPD_declampage_cote_2	|		|	continu	|		|		|
|	NORAD_declampage_cote_2	|		|	continu	|		|		|
|	PEEP_declampage_cote_2	|		|	continu	|		|		|
|	Bicarbonates_declampage_cote_2	|		|	continu	|		|		|
|	NO_declampage_cote_2	|		|	oui = 1 , non = 0	|		|		|
|	Evolution_PAP_declampage_cote_2	|		|	diminution ou augmentation ou stabilité	|		|		|
|	SvO2_declampage_cote_2	|		|	continu	|		|		|
|	Lactates_declampage_cote_2	|		|	continu	|		|		|
|	Ic_declampage_cote_2	|		|	continu	|		|		|
|	Hb_declampage_cote_2	|		|	continu	|		|		|
|	Qc_declampage_cote_2	|		|	continu	|		|		|
|	Examen_Echographique_declampage_cote_2	|		|	text	|		|		|
|	evenements_declampage_cote_2	|		|	oui = 1 , non = 0	|		|		|
|	evenements_declampage_cote_2_commentaires	|		|	text	|		|		|
|	Saigement_estime_declampage_cote2	|		|	continu	|		|		|
|	classification_bullage_2	|		|	 0 = pas de bulles, 1 = Bullage minime, 2 = bullage modéré,  3 = bullage majeur	|		|		|
|	duree_bullage_2	|		|	< 20 sec ; 20 à 60 sec ; 1 à 3 min ; > 3 min	|		|		|
|	retentissement_ETO_bullage_2	|		|	oui = 1 , non = 0	|		|		|
|	retentissement_ECG_bullage_2	|		|	oui = 1 , non = 0	|		|		|
|	retentissement_BIS_bullage_2	|		|	oui = 1 , non = 0	|		|		|
|	Retentissement_hemodynamique_bullage_2	|		|	oui = 1 , non = 0	|		|		|
|	Problemes_survenus_VBP_2	|		|	oui = 1 , non = 0	|		|		|
|	Problemes_survenus_VBP_2_commentaires	|		|	text	|		|		|
|	postoperative_ECMO	|		|	oui = 1 , non = 0	|		|		|
|	only_intraoperative_ECMO	|		|	oui = 1 , non = 0	|		|		|
|	ECMO_during_surgery	|		|	oui = 1 , non = 0	|		|		|
|	ECMO_duration	|		|	continu	|		|		|
|	CEC.1	|		|	oui = 1 , non = 0	|		|		|
|	moment_de_pose_ECMO	|		|	induction = 1 , dissection1er cote = 2 , clampage1er cote = 3 , declampage1er cote = 4 , dissection2eme cote = 5 , clampage2eme cote = 6 , fin chirurgie = 7	|		|		|
|	cause_ECMO	|		|	cause de l ecmo hémodynamique = 1 , hypoxemie = 2 , hypercapnie = 3 , rien = 0 hypoxemie+hypercapnie = 4 , hdm+respi = 5 , prophyactique = 6	|		|		|
|	pulmonary_reduction	|		|	rien = 0 , segmentectomie = 1 , lobectomie unilaterale = 2 , lobectomie bilaterale = 3	|		|		|
|	adrenaline_perop	|		|	oui = 1 , non = 0	|		|		|
|	FiO2_fermeture	|		|	continu	|		|		|
|	PH_fermeture	|		|	continu	|		|		|
|	PAPS_fermeture	|		|	continu	|		|		|
|	PA_fermeture	|		|	continu	|		|		|
|	VT_fermeture	|		|	continu	|		|		|
|	PaCO2_fermeture	|		|	continu	|		|		|
|	PAPM_fermeture	|		|	continu	|		|		|
|	FC_fermeture	|		|	continu	|		|		|
|	Fr_fermeture	|		|	continu	|		|		|
|	PaO2_fermeture	|		|	continu	|		|		|
|	PAPD_fermeture	|		|	continu	|		|		|
|	NORAD_fermeture	|		|	continu	|		|		|
|	PEEP_fermeture	|		|	continu	|		|		|
|	Bicarbonates_fermeture	|		|	continu	|		|		|
|	NO_fermeture	|		|	oui = 1 , non = 0	|		|		|
|	Evolution_fermeture	|		|	text	|		|		|
|	SvO2_fermeture	|		|	continu	|		|		|
|	Lactates_fermeture	|		|	continu	|		|		|
|	Ic_fermeture	|		|	continu	|		|		|
|	Hb_fermeture	|		|	continu	|		|		|
|	Qc_fermeture	|		|	continu	|		|		|
|	Fibroscopie_fermeture	|		|	text	|		|		|
|	Extubation_commentaire	|		|	text	|		|		|
|	VNI	|		|	oui = 1 , non = 0	|		|		|
|	Analgesie_post_operatoire	|		|	text	|		|		|
|	Peridurale_fermeture	|		|	oui = 1 , non = 0	|		|		|
|	PRDC_intraop|		|	continu	|		|		|
|	CEC	|		|	oui = 1 , non = 0	|		|		|
|	ECMO	|		|	oui = 1 , non = 0	|		|		|
|	FFP_intraop	|		|	continu	|		|		|
|	platelets_intraop	|		|	continu	|		|		|
|	NO_per_op	|		|	oui = 1 , non = 0	|		|		|
|	NO_dependence	|		|	oui = 1 , non = 0	|		|		|
|	cause_NO_dependance	|		|	 hypox 1 htpa 2 mixte 3	|		|		|
|	adre_end_surgery	|		|	oui = 1 , non = 0	|		|		|
|	nad_end_surgery	|		|	continu	|		|		|
|	Novoseven_fermeture	|		|	oui = 1 , non = 0	|		|		|
|	estimated_blood_loss	|		|	continu	|		|		|
|	Fibrinogene_fermeture	|		|	continu	|		|		|
|	Cell_Saver	|		|	oui = 1 , non = 0	|		|		|
|	Diurese_fermeture	|		|	continu	|		|		|
|	fluid_support	|		|	continu	|		|		|
|	Drains_D_fermeture	|		|	continu	|		|		|
|	Drains_G_fermeture	|		|	continu	|		|		|
|   Albumine 20% fermeture|||||

</div>
<div id="patient_postoperative">

#### Patient Postoperative
|	Colonne	|	Unité	|	Description	|	Etendue	|	Normalité	|
|	----	|	----	|	----	|	----	|	----	|
|	LOS_first_ventilation	|		|	continu	|		|		|
|	LOS_total_ventilation	|		|	continu	|		|		|
|	 immediate_extubation	|		|	oui = 1 , non = 0	|		|		|
|	secondary_intubation	|		|	oui = 1 , non = 0	|		|		|
|	time_to_secondary_intubation	|		|	continu	|		|		|
|	secondary_ECMO	|		|	oui = 1 , non = 0	|		|		|
|	delai_recours_ECMO	|		|	continu	|		|		|
|	Cause_ECMO_secondaire	|		|	HDM = 1, respir = 2, MIXTE = 3	|		|		|
|	postoperative_vasopressive_support	|		|	 oui = 1 , non = 0	|		|		|
|	ACFA	|		|	 oui = 1 , non = 0	|		|		|
|	PRBC_postop	|		|	continu	|		|		|
|	FFP_postop	|		|	continu	|		|		|
|	Platelets_postop	|		|	continu	|		|		|
|	CVA	|		|	oui = 1 , non = 0	|		|		|
|	hemodyalisis	|		|	oui = 1 , non = 0	|		|		|
|	tracheostomy	|		|	oui = 1 , non = 0	|		|		|
|	reoperation_for_bleeding	|		|	oui = 1 , non = 0	|		|		|
|	bleeding	|		|	oui = 1 , non = 0	|		|		|
|	lower_limb_complication	|		|	oui = 1 , non = 0	|		|		|
|	lower_limb_ischemia	|		|	oui = 1 , non = 0	|		|		|
|	scarpa_complication	|		|	oui = 1 , non = 0	|		|		|
|	vascular_complications	|		|	oui = 1 , non = 0	|		|		|
|	thromboembolic_complication	|		|	oui = 1 , non = 0	|		|		|
|	choc_septique	|		|	oui = 1 , non = 0	|		|		|
|	cardiac_arrest_during_surgery	|		|	oui = 1 , non = 0	|		|		|
|	LOS_ICU	|		|	continu	|		|		|
|	LOS_hosp	|		|	continu	|		|		|
|	in_hospital_mortality	|		|	 oui = 1 , non = 0	|		|		|
|	30_d_survival	|		|	 oui = 1 , non = 0	|		|		|
|	P_F_H0	|		|	 oui = 1 , non = 0	|		|		|
|	PGD_H0	|		|	 oui = 1 , non = 0	|		|		|
|	P_F_end_surgery	|		|	 oui = 1 , non = 0	|		|		|
|	PGD_end_surgery	|		|	continu	|		|		|
|	time_last_PF	|		|	continu	|		|		|
|	PDG_h24	|		|	0 = PGD<3 ; 1 = grade 3 ; E = ECMO ; NF = non fourni	|		|		|
|	PGD_h48	|		|	0 = PGD<3 ; 1 = grade 3 ; E = ECMO ; NF = non fourni	|		|		|
|	PGD3	|		|	0 = PGD<3 ; 1 = grade 3 ; E = ECMO ; NF = non fourni	|		|		|
|	date_de_deces	|		|	date	|		|		|
|	Survival_days_27_10_2018	|		|	continu	|		|		|

</div>
<div id="donor">

#### Donor
|   Colonne |   Unité   |   Description |   Etendue |   Normalité   |
|   ----    |   ----    |   ----    |   ----    |   ----    |
|   CMV_donneur |       |   positif ou negatif  |       |       |
|   EBV_donneur |       |   positif ou negatif  |       |       |
|   Age_donor   |   Int |   continu |       |       |
|   Sex_donor   |   Int |   homme = 1 , femme = 0   |       |       |
|   BMI_donor   |   Int |   Indice de masse corporel du donneur | 13 - 50 | 17 - 25 |
|   Poids_donor |       |   Poids du donneur. En Kg.    |       |       |
|   Taille_donor    |       |   Taille du donneur. En cm.   |       |       |
|   Donneur_CPT |       |   continu |       |       |
|   Tabagisme_donor |       |   oui = 1 , non = 0   |       |       |
|   Aspirations_donor   |       |    aucune = 0 , mineur propre = 1 , moderee = 2 , majeur sales = 3 , NA = 4   |       |       |
|   RX_donor    |       |   normale = 1 , minime = 2 , opacite <1 lobe = 3 , opacite > 1 lobe = 4 , NA = 5  |       |       |
|   PF_donor    |       |   Le ratio p/f mesure la capacité d’un poumon à faire des échanges gazeux.    |       |   Normal: >500, Insuffisant: < 300    |
|   oto_score   |   Int |       |       |       |

</div>
</div>

<div id="target">

#### Target variable

La variable target est définie comme le succès de l'operation que nous essayons de prédire. Nous distinguons les cas suivants:

- Succès A: le patient a été extubé immédiatement à la fin du bloc opératoire et n'a pas été réintubé par la suite. Cela correspond à l'opérateur logique:

```
Immediate_extubation = 1 AND secondary_intubation = 0
```

Succes B: Le patient n'a pas été extubé immédiatement à la fin du bloc opératoire, n'a pas été réintubé par la suite et est resté moins de 48h sous assistance, durée pendant laquelle il n'est pas décédé. Cette condition correspond à l'opérateur logique:

```
Immediate_extubation = 0 AND secondary_intubation = 0 AND LOS_first_ventilation < 2 AND Survival_days >= 2
```
- Echec: tous les autres cas.

</div>

<div id="dynamic_variables">

### Variable Dynamiques
Le fichier `clean/dynamic.csv` contient les mesures prises chaque minute par les instruments de mesure lors de l'opération.

Pour chaque ligne, le patient et le timestamp de la mesure sont identifiés par :

|  Colonne   | Unité | Description                     |
| -----------| ------ | ------------------------------- |
| id_patient | id     | identifiant unique d'un patient |
| time       | HH:MM  | timestamp de la mesure          |



Les autres colonnes représentent les diverses mesures effectuées. Elles peuvent être subdivisées en 4 catégories :
- <a href="#haemodynamic">**Haemodynamic**</a> : mesures des capacités haemodynamique
- <a href="#respiratory">**Respiratory**</a> : mesures des capacités respiratoires
- <a href="#neurology">**Neurology**</a> : mesures des capacités neurologiques
- <a href="#temperature">**Temperature**</a> : mesures de la température

Ces dernières sont détaillées dans les sections qui suivent.

<div id="haemodynamic">

#### Haemodynamic
| Colonne | Unité | Description | Etendue | Normalité | Commentaires |
| --------| ----- | ----------- | ------- | -------- | -------- |
| DC | L/min | Debit cardiaque. | 0,5 - 10 | 2 - 5. < 2 anormalité |
| FC | /min | fréquence cardiaque | 0 - 220 | 50 - 90 | > 120 alerte  <br/> > 150 anomalie cardiologique <br/> < 30 anomalie cardiologique  <br/> 0 Arrêt cardiaque Si TAS effondrée|
| PAPdia | mmHg | Pression artérielle pulmonaire diastolique | 0 - 65 | 14 - 35 | possible 0 si absente|
| PAPmoy | mmHg | Pression artérielle moyenne  | 0 - 65 | 20 - 35 | |
| PAPsys | mmHg | pression artère pulmonaire systolique | 0 - 120 | 25 - 40 | > 50 danger <br/> si valeur = ou > PAS s recours à une assistance externe|
| PASd | mmHg | Pression artérielle pulmonaire diastolique | 0 - 80 | 35 - 60 | |
| PASm | mmHg | Pression artérielle moyenne  | 0 - 150 | 50 - 90 | > 60 objectif pendant l'opératioin <br/> < 40 sévérité de la situation |
| PASs | mmHg | pression artérielle systolique | 0 - 320 | 80 - 140 | < 70 sévérité|
| PNId | mmHg | Pression non invasive diastolique | 0 - 80 | 35 - 60 | |
| PNIm | mmHg | pression non invasive moyenn | 0 - 150 | 50 - 90 | > 60 objectif pendant l'opération <br/> < 40 sévérité de la situation |
| PNIs | mmHg | pression non invasive systolique | 0 - 320 | 80 - 140 | < 70 sévérité |

</div>
<div id="respiratory">

#### Respiratory
| Colonne | Unité | Description | Etendue | Normalité | Commentaires |
| --------| ----- | ----------- | ------- | -------- | -------- |
| ETCO2 | kPa | CO2 expiré = marqueur d'équilibre général | 0 - 10 | 3 - 5.5 | <3 severite  <br/> >6 difficulté ventilatoire |
| ETCO2 (mmHg)  | mmHg | CO2 expiré = marqueur d'équilibre général | 0 - 10 | 3 - 5.5 | <3 severite  <br/> >6 difficulté ventilatoire |
| ETO2 | % | Oxygène expiré | 21 - 100 | 35 - 60 | > 60 si besoin|
| FICO2 | kPa | Fraction inspirée en CO2 | 0 - 5 | 1 - 3 | non informatif |
| FICO2 (mmHg)   | mmHg | Fraction inspirée en CO2 | 0 - 5 | 1 - 3 | non informatif |
| FIN2O | % | fraction inspirée en N20 | 0 - 60 |  | 0 Foch|
| FiO2 | % | fraction inspirée en Oxygène | 21- 100 | 21 - 50 | > 80 si oxygénation difficile|
| FR | /min | fréquence respiratoire | 0 - 60 | 12 - 24 | < 12 problème sévère <br/> > 35 difficultés au bloc|
| FR(ecg) | /min | fréquence respiratoire | 0 -  60 | 12 - 24 | < 12 problème respiratoire <br/> > 35 difficulté au bloc ne considérer que si colonne O absente ou = 0 source depuis l'Electrocardiogramme|
| MAC |  | Concentration alvéolaire moyenne | 0 - 3 | 1 - 2 | 0 si anesthésie intra veineuse|
| PEEPtotal | cmH2O | pression expiratoire positive | 0 - 20 | 4 - 8 | > 8 poumon pathologique|
| Pmax | cmH2O | pression maximale | 0 - 65 | 25 -  40 | > 40 poumon anormal|
| Pmean | cmH2O | Pression moyenne | 0 - 40 | 8 - 25 | > 30 poumon pathologique|
| Pplat | cmH2O | pression plateau | 0 - 40 | 8 - 25 | > 30 poumon pathologique|
| RR(co2) | /min | respiratory rate | 0 - 60 | 12 - 24 | < 12 problème sévère <br/> > 35 difficultés au bloc |
| SpO2 | % | Saturation pulsée en oxygène | 0 - 100 | 92 - 100 | < 90 événement notable <br/> < 80 événement grave |
| SvO2 (m) | % | saturation veineuse en oxygène | 0 - 100 | 75 - 88 | > 92 problable malposition du capteur <br/> < 60 gravité sévère|
| VT | ml | volume respiratoire | 0 - 900   | 300 - 450 | |

</div>
<div id="neurology">

#### Neurology
| Colonne | Unité | Description | Etendue | Normalité | Commentaires |
| --------| ----- | ----------- | ------- | -------- | -------- |
| B.I.S |  | profondeur du sommeil index bispectral | 0 - 100 | 40 - 60 | > 70 mémorisation <br/> < 40 sommeil trop profond  <br/> 0 artefact si BIS SR 0 <br/> 0 valeur à considérer si BIS SR>0|
| BIS SR | % | EEG plat | 0 - 100 | 0 | > 10 anormal|
| ET Des. | % | Agent sedatif | 1 - 12 |  | rarement utilisé dans la transplantation|
| ET Sevo. | % | Agent sedatif | 1 - 6 |  2| rarement utilisé dans la transplantation|
| NMT TOF |  | relaxation musculaire Train of For | 0 - 4 | 0 - 1 | 0 voir colonne S <br/> > 3 pour réveil possible|
| NMTratio | % | relaxation musculaire ratio | 0 - 100 | 0 - 100 | valeur si 4 à la colonne R <br/> > 50% réveil possible|

</div>
<div id="temperature">

#### Temperature
| Colonne | Unité | Description | Etendue | Normalité | Commentaires |
| --------| ----- | ----------- | ------- | -------- | -------- |
| Temp | °C | température | 0 - 50 | 34 - 37 | > 38 infection débutante|

</div>
</div>
</div>
