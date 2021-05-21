SEX_CHOICES = (
    (1,  'male'),
    (2,  'female'),
)

GENDER = (
    (1,  'male'),
    (2,  'female'),
    (3, 'other'),
)

MARITAL_STATUS = (
    (1, 'Minor'),
    (2, 'Married'),
    (3, 'Single'),
    (4, 'Divorced'),
    (5, 'Widowed'),
)

RACE_ETHNICITY = (
    (1, 'African American/Black'),
    (2, 'White'),
    (3, 'Asian'),
    (4, 'Hispanic'),
    (5, 'American Indian or Alaska Native'),
    (6, 'Pacific Islander'),
    (7, 'Other'),
)

PRIMARY_SUBSCRIBER_1 = (
    (1, 'Self'),
    (2, 'Spouse'),
    (3, 'Parent'),
    (4, 'Other'),
)

PRIMARY_SUBSCRIBER_2 = (
    (1, 'Self'),
    (2, 'Spouse'),
    (3, 'Parent'),
    (4, 'Other'),
)

HIGHEST_LEVEL_OF_EDUCATION = (
    (1, 'High School'),
    (2, 'College')
)

SYMPTOM_SCALE = (
    (0, 'None'),
    (1, 'Less Often'),
    (2, 'Moderate'),
    (3, 'More Often'),
    (4, 'Severe'),
)

(CRYING, TIREDNESS, DREAD, HOPELESSNESS, HEADACHES, VOICES, IMPULSE, 
APPETITE, ACTIVITIES, NTEREST_IN_SEX, NERVOUSNESS, NIGHTMARES, PANIC, 
CONCENTRATION, MEMORY, SADNESS, SLEEP, SUICIDAL, SUSPICIOUSNESS, 
WEIGHT_LOSS, WORRY, OTHERS) = SYMPTOM_SCALE

HEALTH_HISTORY = (
    (1, 'BLOOD PRESSURE'),
    (2, 'DIABETES'),
    (3, 'ASTHMA'),
    (4, 'CORONARY'),
    (5, 'SURGICAL'),
    (6, 'OTHER'),
)

ACTIVITY_SCORE_1 = (
    (0, 'None'),
    (1, '< 1 hr/day'),
    (2, '1-3 hr/day'),
    (3, '3-8 hr/day'),
    (4, '> 8 hr/day'),
)

ACTIVITIY_SCORE_2 = (
    (0, 'None'),
    (1, 'Slightly'),
    (2, 'Definitely, But Manageable'),
    (3, 'Substantially'),
    (4, 'Extremely'),
)

ACTIVITY_SCORE_3 = (
    (0, 'None'),
    (1, 'Mild'),
    (2, 'Moderate'),
    (3, 'Severe'),
    (4, 'Near Constant')
)

ACTIVITY_SCORE_4 = (
    (0, 'Complete Control'),
    (1, 'Most Of The Time'),
    (2, 'Sometimes'),
    (3, 'Often'),
    (4, 'Never'),
)

ACTIVITY_SCORE_5 = (
    (0, 'No Anxiety'),
    (1, 'Mild Anxiety'),
    (2, 'Moderate Anxiety'),
    (3, 'Prominent Anxiety'),
    (4, 'Extreme Anxiety')
)

OBSESSIVE_THOUGTS, COMPULSIVE_BEHAVIORS = ACTIVITY_SCORE_1

OBSESSIVE_THOUGTS_SOCIAL, COMPULSIVE_BEHAVIORS_SOCIAL = ACTIVITIY_SCORE_2

DISTRESS = ACTIVITY_SCORE_3

RESIST_OBSESSIVE_THOUGTS, RESIST_COMPULSIONS = ACTIVITY_SCORE_4

OBSESSIVE_THOUGTS_CONTROL, COMPULSION_CONTROL = ACTIVITY_SCORE_5

ACTIVITY_PROBLEMS = (
    (1, 'It has no problem'),
    (2, 'It was a minor problem'),
    (3, 'It was a moderate problem'),
    (4, 'It was a serious problem'),
)

HEALTH_QUESTIONNAIRE = (
    (0, 'Not at all'),
    (1, 'Several days'),
    (2, 'More than half the days'),
    (3, 'Nearly every day'),
)

(LITTLE_PLEASURE, DEPRESSED, TROUBLE_SLEEPING, LITTLE_ENERGY, 
POOR_APPETITE, FEELING_BAD, TROUBLE_CONCENTRATING, SLOWLY_OR_FIGETY,
THOUGHTS_OF_DEATH_OR_HURTING) = HEALTH_QUESTIONNAIRE

QUESTIONNAIRE_DIFFICULTY = (
    (1, 'Not difficult at all'),
    (2, 'Somewhat difficult'),
    (3, 'Very difficult'),
    (4, 'Extremely difficult'),
)

AUTHORIZE_RELEASE = (
    (1, 'All health information')
    (2, 'Only the following records'),
)

AUTHORIZED_HEALTH_INFO = (
    (1, 'Mental Health Information'),
    (2, 'Alcohol/Drug Treatment Information')
)

