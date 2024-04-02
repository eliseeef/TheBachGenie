const jsObject = {
  "season_17.json": [
    {
      Name: "Catherine Giudici",
      Age: "26",
      Hometown: "Seattle, Washington",
      Occupation: "Graphic Designer",
      Eliminated: "Winner",
      Place: "1",
    },
    {
      Name: "Lindsay Yenter",
      Age: "24",
      Hometown: "Fort Leonard Wood, Missouri",
      Occupation: "Substitute Teacher",
      Eliminated: "Runner-up",
      Place: "2",
    },
  ],
  "season_10.json": [
    {
      Name: "Tessa Horst",
      Age: "26",
      Hometown: "San Francisco, California",
      Occupation: "Social Worker",
      Eliminated: "Winner",
    },
    {
      Name: "Bevin Nicole Powers",
      Age: "28",
      Hometown: "Palo Alto, California",
      Occupation: "Assistant",
      Eliminated: "Week 8",
    },
  ],
};

// Denormalize the season onto each person
const processed = Object.keys(jsObject).reduce((acc, season) => {
  jsObject[season].forEach((person) => {
    acc[person.Name] = {
      ...person,
      season,
    };
  });
  return acc;
}, {});

const sortedBySeason = Object.entries.reduce((acc, [name, person]) => {
  if (!acc[person.season]) {
    acc[person.season] = [];
  }
  acc[person.season].push(person);
  return acc;
}, {});

const list = Object.values(processed).sort((a, b) =>
  a.season.localeCompare(b.season)
);

const contestants = [
  {
    Name: "Amanda Marsh",
    Age: 23,
    Hometown: "Chanute, Kansas",
    Job: "Event Planner",
    Eliminated: "Winner",
    season: "01",
  },
  {
    Name: "Trista Rehn",
    Age: 29,
    Hometown: "St. Louis, Missouri",
    Job: "Miami Heat Dancer",
    Eliminated: "Runner-up",
    season: "01",
  },
  {
    Name: "Shannon Oliver",
    Age: 24,
    Hometown: "Dallas, Texas",
    Job: "Financial Management Consultant",
    Eliminated: "Week 5",
    season: "01",
  },
  {
    Name: "Kimberly Karels",
    Age: 24,
    Hometown: "Tempe, Arizona",
    Job: "Nanny",
    Eliminated: "Week 4",
    season: "01",
  },
  {
    Name: "Marissa May",
    Age: 26,
    Hometown: "Southwest",
    "Job category": "PR",
    Race: "White",
    Place: "9",
    season: "15",
  },
  {
    Name: "Ashley Spivey",
    Age: 26,
    Hometown: "Mid atlantic",
    "Job category": "NANNY",
    Race: "White",
    Place: "11",
    season: "15",
  },
  {
    Name: "Lindsay Hill",
    Age: 25,
    Hometown: "Southwest",
    "Job category": "TEACHER",
    Race: "White",
    Place: "12",
    season: "15",
  },
  {
    Name: "Meghan Merritt",
    Age: 30,
    Hometown: "East",
    "Job category": "MARKETING",
    Race: "White",
    Place: "12",
    season: "15",
  },
  {
    Name: "Stacey Quirpel",
    Age: 26,
    Hometown: "East",
    "Job category": "RESTAURANT JOB",
    Race: "White",
    Place: "12",
    season: "15",
  },
];

// Weeks 1 - 10
// There are no outliers, so we'll use unsupervised descretization
// Low Weeks 1 - 4
// Medium Weeks 5 - 7
// High Weeks 8 - 10
// Winner

const turnWeeksIntoCategory = (weeks) => {
  if (weeks <= 4) {
    return "Low";
  }
  if (weeks <= 7) {
    return "Medium";
  }
  if (weeks <= 10) {
    return "High";
  }
  return "Winner";
};

const turnPlaceIntoCategory = (place) => {
  if (place <= 3) {
    return "High";
  }
  if (place <= 8) {
    return "Medium";
  }
  return "Low";
};

const parseWeeks = (person) => {
  if (
    "Eliminated" in person &&
    person.Eliminated !== null &&
    person.Eliminated.includes("Week")
  ) {
    const weeks = person.Eliminated.split(" ")[1];
    return turnWeeksIntoCategory(weeks);
  }
  if ("Place" in person) {
    if (person.Place === "Winner") {
      return "Winner";
    }
    if (person.Place.includes("–")) {
      const [low, high] = person.Place.split("–");
      return turnPlaceIntoCategory(low);
    }
    return turnPlaceIntoCategory(+person.Place);
  }
};

const process = contestants.reduce((acc, person) => {
  acc.push(person);
  return acc;
}, []);
