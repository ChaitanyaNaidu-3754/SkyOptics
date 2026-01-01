"""
Astronomy Data Service - Local data for CosmosAI
No external API dependencies - works offline!
"""

# Real 2026 Astronomy Events
ASTRONOMY_EVENTS_2026 = [
    {"date": "Jan 3, 2026", "event": "Quadrantids Meteor Shower Peak", "desc": "Up to 120 meteors per hour. Best viewed after midnight."},
    {"date": "Jan 10, 2026", "event": "Jupiter at Opposition", "desc": "Jupiter at its closest and brightest. Visible all night."},
    {"date": "Feb 1, 2026", "event": "Venus at Greatest Elongation", "desc": "Venus at peak visibility in evening sky."},
    {"date": "Feb 28, 2026", "event": "Seven Planet Alignment", "desc": "Rare alignment of 7 planets visible before sunrise."},
    {"date": "Mar 3, 2026", "event": "Total Lunar Eclipse", "desc": "Blood Moon visible from Americas, Europe, Africa."},
    {"date": "Mar 14, 2026", "event": "Pi Day Meteor Watch", "desc": "Minor meteor activity, great for beginners."},
    {"date": "Apr 22, 2026", "event": "Lyrids Meteor Shower", "desc": "18 meteors per hour, bright fireballs possible."},
    {"date": "May 6, 2026", "event": "Eta Aquarids Peak", "desc": "Debris from Halley's Comet, 30 meteors/hour."},
    {"date": "Jun 21, 2026", "event": "Summer Solstice", "desc": "Longest day of the year in Northern Hemisphere."},
    {"date": "Jul 28, 2026", "event": "Delta Aquarids Peak", "desc": "20 meteors per hour, best after midnight."},
    {"date": "Aug 12, 2026", "event": "Perseids Meteor Shower", "desc": "Best meteor shower! Up to 100 meteors per hour."},
    {"date": "Aug 12, 2026", "event": "Partial Solar Eclipse", "desc": "Visible from parts of North America."},
    {"date": "Sep 7, 2026", "event": "Saturn at Opposition", "desc": "Saturn at its brightest, rings clearly visible."},
    {"date": "Oct 21, 2026", "event": "Orionids Peak", "desc": "Fast meteors from Halley's Comet debris."},
    {"date": "Nov 5, 2026", "event": "Taurids Peak", "desc": "Slow, bright fireballs - great for photos."},
    {"date": "Nov 17, 2026", "event": "Leonids Meteor Shower", "desc": "15 meteors per hour, historically spectacular."},
    {"date": "Dec 13, 2026", "event": "Geminids Peak", "desc": "King of meteor showers! 150 multicolored meteors/hour."},
    {"date": "Dec 21, 2026", "event": "Winter Solstice", "desc": "Shortest day, longest night for stargazing."},
]

# Dark Sky Locations by City
DARK_SKY_LOCATIONS = {
    "default": [
        {"name": "Local Rural Area", "distance": "30-50 km from city center", "bortle": 4, "rating": "Good", "tip": "Drive away from city lights for 30+ minutes"},
        {"name": "Nearby Hills/Mountains", "distance": "50-100 km", "bortle": 3, "rating": "Very Good", "tip": "Higher elevation = clearer skies"},
        {"name": "Designated Dark Sky Park", "distance": "Check darksky.org for nearest", "bortle": 2, "rating": "Excellent", "tip": "Best for astrophotography"},
    ],
    
    # India
    "mumbai": [
        {"name": "Igatpuri", "distance": "120 km", "bortle": 4, "rating": "Good", "tip": "Best during new moon nights"},
        {"name": "Lonavala Hills", "distance": "85 km", "bortle": 4, "rating": "Good", "tip": "Go past the town for darker skies"},
        {"name": "Malshej Ghat", "distance": "130 km", "bortle": 3, "rating": "Very Good", "tip": "Excellent during monsoon break"},
        {"name": "Jawhar", "distance": "150 km", "bortle": 3, "rating": "Very Good", "tip": "Less crowded, pristine skies"},
    ],
    "delhi": [
        {"name": "Sariska Tiger Reserve", "distance": "200 km", "bortle": 3, "rating": "Very Good", "tip": "Stay overnight for best experience"},
        {"name": "Neemrana", "distance": "120 km", "bortle": 4, "rating": "Good", "tip": "Quick getaway, decent skies"},
        {"name": "Damdama Lake", "distance": "55 km", "bortle": 5, "rating": "Fair", "tip": "Close but light pollution present"},
        {"name": "Ladakh (Hanle)", "distance": "Flight required", "bortle": 1, "rating": "World Class", "tip": "India's darkest skies, high altitude"},
    ],
    "bangalore": [
        {"name": "Savandurga", "distance": "60 km", "bortle": 4, "rating": "Good", "tip": "Rocky hilltop, good horizon"},
        {"name": "Anthargange", "distance": "70 km", "bortle": 4, "rating": "Good", "tip": "Cave camping available"},
        {"name": "Coorg", "distance": "250 km", "bortle": 3, "rating": "Very Good", "tip": "Coffee estates offer clear views"},
        {"name": "Yelagiri", "distance": "160 km", "bortle": 3, "rating": "Very Good", "tip": "Hill station with dark skies"},
    ],
    "chennai": [
        {"name": "Yelagiri Hills", "distance": "230 km", "bortle": 3, "rating": "Very Good", "tip": "Best in Tamil Nadu for stargazing"},
        {"name": "Mahabalipuram Beach", "distance": "60 km", "bortle": 5, "rating": "Fair", "tip": "Ocean horizon, some light pollution"},
        {"name": "Jawadhu Hills", "distance": "200 km", "bortle": 3, "rating": "Very Good", "tip": "Tribal area, very dark"},
    ],
    "hyderabad": [
        {"name": "Ananthagiri Hills", "distance": "80 km", "bortle": 4, "rating": "Good", "tip": "Popular weekend spot"},
        {"name": "Nallamala Forest", "distance": "150 km", "bortle": 3, "rating": "Very Good", "tip": "Tiger reserve, pristine darkness"},
        {"name": "Pocharam Wildlife Sanctuary", "distance": "100 km", "bortle": 3, "rating": "Very Good", "tip": "Lake reflects stars beautifully"},
    ],
    
    # USA
    "new york": [
        {"name": "Cherry Springs State Park", "distance": "400 km", "bortle": 2, "rating": "Excellent", "tip": "One of the darkest spots on East Coast"},
        {"name": "Catskill Mountains", "distance": "160 km", "bortle": 4, "rating": "Good", "tip": "Accessible weekend trip"},
        {"name": "Harriman State Park", "distance": "65 km", "bortle": 5, "rating": "Fair", "tip": "Closest dark-ish option"},
    ],
    "los angeles": [
        {"name": "Joshua Tree National Park", "distance": "220 km", "bortle": 3, "rating": "Very Good", "tip": "Designated Dark Sky Park"},
        {"name": "Death Valley", "distance": "450 km", "bortle": 1, "rating": "World Class", "tip": "Darkest skies in USA"},
        {"name": "Angeles National Forest", "distance": "80 km", "bortle": 4, "rating": "Good", "tip": "Quick escape from LA lights"},
    ],
    "chicago": [
        {"name": "Starved Rock State Park", "distance": "160 km", "bortle": 4, "rating": "Good", "tip": "Beautiful canyons too"},
        {"name": "Indiana Dunes", "distance": "80 km", "bortle": 5, "rating": "Fair", "tip": "Lake views, moderate darkness"},
    ],
    
    # UK
    "london": [
        {"name": "South Downs National Park", "distance": "90 km", "bortle": 4, "rating": "Good", "tip": "Designated Dark Sky Reserve"},
        {"name": "Exmoor National Park", "distance": "280 km", "bortle": 2, "rating": "Excellent", "tip": "Europe's first Dark Sky Reserve"},
        {"name": "Brecon Beacons", "distance": "250 km", "bortle": 3, "rating": "Very Good", "tip": "Welsh mountains, exceptional darkness"},
    ],
    
    # Australia
    "sydney": [
        {"name": "Blue Mountains", "distance": "100 km", "bortle": 4, "rating": "Good", "tip": "Head to Blackheath area"},
        {"name": "Warrumbungle National Park", "distance": "450 km", "bortle": 2, "rating": "Excellent", "tip": "Australia's first Dark Sky Park"},
        {"name": "Mudgee", "distance": "270 km", "bortle": 3, "rating": "Very Good", "tip": "Wine country with dark skies"},
    ],
    "melbourne": [
        {"name": "Grampians National Park", "distance": "260 km", "bortle": 3, "rating": "Very Good", "tip": "Outback-like darkness"},
        {"name": "Mornington Peninsula", "distance": "80 km", "bortle": 5, "rating": "Fair", "tip": "Coastal views, some light pollution"},
    ],
}

# Seasonal Constellation Data
CONSTELLATION_DATA = {
    "winter_north": {
        "constellations": ["Orion", "Taurus", "Gemini", "Canis Major", "Auriga"],
        "highlight": "Orion the Hunter - Look for the three belt stars",
        "best_time": "January-February, 9 PM - 2 AM",
        "mythology": "Orion was a giant huntsman placed among the stars by Zeus"
    },
    "spring_north": {
        "constellations": ["Leo", "Virgo", "Boötes", "Ursa Major", "Hydra"],
        "highlight": "Leo the Lion - The sickle asterism is unmistakable",
        "best_time": "April-May, 9 PM - midnight",
        "mythology": "Leo represents the Nemean Lion slain by Hercules"
    },
    "summer_north": {
        "constellations": ["Cygnus", "Lyra", "Aquila", "Scorpius", "Sagittarius"],
        "highlight": "Summer Triangle - Vega, Deneb, and Altair",
        "best_time": "July-August, 10 PM - 3 AM",
        "mythology": "The Milky Way runs through the Summer Triangle"
    },
    "fall_north": {
        "constellations": ["Pegasus", "Andromeda", "Perseus", "Cassiopeia", "Cepheus"],
        "highlight": "Andromeda Galaxy - Visible to naked eye!",
        "best_time": "October-November, 8 PM - 1 AM",
        "mythology": "Princess Andromeda was chained to rocks as sacrifice to a sea monster"
    }
}

# Image Pattern Detection Keywords
CELESTIAL_PATTERNS = {
    "orion": {
        "name": "Orion Constellation",
        "description": "The Hunter - one of the most recognizable constellations",
        "mythology": "Greek hunter, placed in the sky by Zeus. Associated with winter.",
        "best_visible": "December to February in Northern Hemisphere",
        "next_appearance": "Visible every winter night, peaks in January"
    },
    "big_dipper": {
        "name": "Big Dipper (Ursa Major)",
        "description": "The Great Bear - a famous asterism and navigation aid",
        "mythology": "Callisto transformed into a bear by Hera, placed in sky by Zeus",
        "best_visible": "Year-round in Northern Hemisphere, best in Spring",
        "next_appearance": "Always visible above 41°N latitude"
    },
    "milky_way": {
        "name": "Milky Way Band",
        "description": "Our galaxy's disk seen edge-on - billions of stars",
        "mythology": "In Greek myth, milk spilled from Hera created the celestial river",
        "best_visible": "June to September, requires dark skies (Bortle 4 or darker)",
        "next_appearance": "Core visible summer nights in dark locations"
    },
    "meteor": {
        "name": "Meteor/Shooting Star",
        "description": "Space debris burning up in Earth's atmosphere",
        "mythology": "Ancient cultures saw them as souls, omens, or divine arrows",
        "best_visible": "During meteor showers (Perseids in August, Geminids in December)",
        "next_appearance": "Quadrantids: Jan 3-4, Perseids: Aug 11-13, Geminids: Dec 13-14"
    },
    "planets": {
        "name": "Planetary Body",
        "description": "Bright, non-twinkling point - likely Venus, Jupiter, Mars, or Saturn",
        "mythology": "Named after Roman gods for their brightness and wandering motion",
        "best_visible": "Varies by planet - check astronomy apps for current positions",
        "next_appearance": "Jupiter at opposition: Jan 10, 2026; Saturn opposition: Sep 7, 2026"
    },
    "moon": {
        "name": "Moon Feature",
        "description": "Earth's natural satellite - craters, maria, or phases visible",
        "mythology": "Selene/Luna in Greek/Roman myth, associated with cycles and tides",
        "best_visible": "Any clear night - full moon for surface features",
        "next_appearance": "Lunar cycle is 29.5 days, full moon every month"
    },
    "nebula": {
        "name": "Nebula / Star Cluster",
        "description": "Fuzzy patch - could be emission nebula, cluster, or galaxy",
        "mythology": "Ancient astronomers called them 'cloudy stars'",
        "best_visible": "Orion Nebula visible naked eye in winter; Andromeda in fall",
        "next_appearance": "M42 Orion Nebula: Dec-Feb; M31 Andromeda: Sep-Nov"
    },
    "star_trail": {
        "name": "Star Trails",
        "description": "Circular patterns from Earth's rotation during long exposure",
        "mythology": "Ancient navigation by finding the celestial pole",
        "best_visible": "Any clear night with long camera exposure (30+ seconds)",
        "next_appearance": "Can be photographed any clear night"
    }
}

# Chat Response Database - Keyword-based Q&A
CHAT_RESPONSES = {
    # Black holes
    "black hole": "A black hole is a region where gravity is so strong that nothing, not even light, can escape. They form when massive stars collapse. The closest known black hole to Earth is about 1,000 light-years away.",
    
    # Stars
    "star": "Stars are massive balls of hot gas (hydrogen and helium) undergoing nuclear fusion. Our Sun is a medium-sized yellow dwarf star. The nearest star to Earth (after the Sun) is Proxima Centauri, 4.24 light-years away.",
    "sun": "The Sun is our closest star, about 150 million km away (1 AU). It's 4.6 billion years old, contains 99.86% of our solar system's mass, and will become a red giant in about 5 billion years.",
    
    # Planets
    "planet": "A planet is a celestial body that orbits a star, has enough mass for spherical shape, and has cleared its orbital neighborhood. Our solar system has 8 planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
    "mars": "Mars is the 4th planet from the Sun, called the Red Planet due to iron oxide. It has the largest volcano (Olympus Mons) and canyon (Valles Marineris) in the solar system. NASA's rovers are currently exploring its surface.",
    "jupiter": "Jupiter is the largest planet in our solar system - 11x Earth's diameter! It has 95+ moons, including Europa (with subsurface ocean). The Great Red Spot is a storm raging for 400+ years.",
    "saturn": "Saturn is famous for its spectacular ring system made of ice and rock. It's the least dense planet - it would float on water! Its moon Titan has a thick atmosphere and liquid methane lakes.",
    "venus": "Venus is Earth's 'twin' in size but has a crushing atmosphere (90x Earth's pressure) and surface temperature of 465°C. It rotates backwards and a day there is longer than its year!",
    "mercury": "Mercury is the smallest planet and closest to the Sun. Despite this, it's not the hottest (Venus is). It has extreme temperatures: 430°C day, -180°C night, and no atmosphere.",
    "uranus": "Uranus is an ice giant that rotates on its side (98° tilt)! It has faint rings and 27 known moons. Its blue-green color comes from methane in its atmosphere.",
    "neptune": "Neptune is the windiest planet with storms reaching 2,100 km/h! It's the farthest planet from the Sun and wasn't discovered until 1846. Its moon Triton orbits backwards.",
    
    # Moon
    "moon": "Earth's Moon is ~4.5 billion years old, likely formed from a collision with a Mars-sized body. It causes our ocean tides, is slowly drifting away (~3.8 cm/year), and is the only world beyond Earth humans have walked on.",
    "lunar eclipse": "A lunar eclipse occurs when Earth passes between the Sun and Moon, casting a shadow. The Moon turns red during totality (Blood Moon) due to Earth's atmosphere filtering sunlight. The next total lunar eclipse is March 3, 2026.",
    "solar eclipse": "A solar eclipse occurs when the Moon passes between Earth and Sun. Total solar eclipses are rare at any location because the Moon's shadow is small. NEVER look directly at a solar eclipse without proper eye protection!",
    
    # Constellations
    "constellation": "Constellations are patterns of stars as seen from Earth, used for navigation and storytelling since ancient times. There are 88 official constellations. They help us locate celestial objects and track seasons.",
    "orion": "Orion is one of the most recognizable constellations, visible worldwide. Look for the 3 belt stars. The Orion Nebula (M42) is visible below the belt - a stellar nursery 1,344 light-years away!",
    "ursa major": "Ursa Major (Great Bear) contains the Big Dipper asterism. The two stars at the end of the 'cup' point to Polaris, the North Star. It's circumpolar in the Northern Hemisphere.",
    "north star": "Polaris (North Star) is located nearly at the celestial north pole. It's actually a triple star system about 433 light-years away. Find it by following the Big Dipper's pointer stars.",
    
    # Galaxy & Universe
    "galaxy": "A galaxy is a massive system of stars, gas, dust, and dark matter held together by gravity. Our Milky Way contains 100-400 billion stars. The observable universe has ~2 trillion galaxies!",
    "milky way": "The Milky Way is our home galaxy - a barred spiral about 100,000 light-years across. Our solar system is located in the Orion Arm, about 26,000 light-years from the center.",
    "andromeda": "Andromeda (M31) is the nearest major galaxy to the Milky Way, 2.5 million light-years away. It's visible to the naked eye and approaching us at 110 km/s - we'll merge in ~4.5 billion years!",
    "universe": "The observable universe is 93 billion light-years in diameter, began with the Big Bang 13.8 billion years ago, and is still expanding! It contains ~2 trillion galaxies.",
    
    # Meteor & Comets
    "meteor": "A meteor is a space rock burning up in Earth's atmosphere - also called a shooting star. Most are the size of grains of sand. If one reaches the ground, it's called a meteorite.",
    "meteor shower": "Meteor showers occur when Earth passes through comet debris trails. The best are Perseids (August), Geminids (December), and Quadrantids (January). Peak rates can reach 100+ meteors per hour!",
    "comet": "Comets are 'dirty snowballs' - ice and rock orbiting the Sun. When close to the Sun, they develop tails up to millions of km long! Famous ones include Halley's (visible every 76 years, next in 2061).",
    
    # Space Exploration
    "iss": "The International Space Station orbits at ~400 km altitude, traveling at 28,000 km/h. It's been continuously inhabited since 2000 and is often visible as a bright moving dot in the night sky.",
    "nasa": "NASA (National Aeronautics and Space Administration) is the US space agency, founded in 1958. Recent projects include Artemis program to return humans to the Moon and the James Webb Space Telescope.",
    "telescope": "Telescopes magnify distant objects using lenses (refractor) or mirrors (reflector). The James Webb Space Telescope is currently the most powerful, observing in infrared from 1.5 million km away.",
    "james webb": "The James Webb Space Telescope launched in 2021 and orbits the L2 point, 1.5 million km from Earth. Its 6.5m mirror observes in infrared, revealing the most distant galaxies ever seen.",
    "hubble": "The Hubble Space Telescope has orbited Earth since 1990, revolutionizing astronomy with stunning images and deep field observations. It has made over 1.5 million observations.",
    
    # Light & Distance
    "light year": "A light-year is the distance light travels in one year: about 9.46 trillion km. It's used for measuring cosmic distances. The nearest star (Proxima Centauri) is 4.24 light-years away.",
    "speed of light": "Light travels at 299,792 km/s (about 300,000 km/s) in vacuum. This is the cosmic speed limit - nothing with mass can reach or exceed it. Light from the Sun takes 8 minutes to reach Earth.",
    
    # Dark Sky & Observation
    "bortle": "The Bortle scale (1-9) measures night sky brightness. 1 = pristine dark sky (can see zodiacal light), 9 = inner city (only bright stars visible). Bortle 4 is excellent for viewing the Milky Way.",
    "dark sky": "Dark sky locations have minimal light pollution, essential for deep-sky observing. Look for designated Dark Sky Parks or drive 50+ km from cities. New moon nights are best.",
    "light pollution": "Light pollution from artificial sources obscures stars and affects wildlife. 80% of the world's population lives under light-polluted skies. Use light pollution maps to find dark spots.",
    
    # General astronomy
    "astronomy": "Astronomy is the scientific study of celestial objects, space, and the physical universe. It's one of the oldest sciences, with records from ancient Babylon, Egypt, and Greece dating back 5,000+ years.",
    "astrophotography": "Astrophotography captures images of celestial objects. Start with a DSLR on a tripod for star trails or Milky Way. Advanced setups use tracking mounts and telescopes for deep sky objects.",
    
    # Fallback responses
    "help": "I can answer questions about: planets, stars, black holes, galaxies, constellations, meteor showers, eclipses, telescopes, space missions, and stargazing tips. Just ask!",
    "hello": "Hello, stargazer! I'm your astronomy assistant. Ask me anything about the cosmos - from planets and stars to black holes and galaxies!",
    "hi": "Hi there! Ready to explore the universe? Ask me about stars, planets, constellations, or any cosmic curiosity you have!",
}

# Default response when no keyword matches
DEFAULT_CHAT_RESPONSE = "That's an interesting astronomy question! I specialize in topics like planets, stars, black holes, galaxies, constellations, meteor showers, and telescopes. Try asking about one of these subjects, or type 'help' for a list of topics I know about."


def get_chat_response(user_message):
    """Find best matching response for user message."""
    message_lower = user_message.lower()
    
    # Check for keyword matches
    for keyword, response in CHAT_RESPONSES.items():
        if keyword in message_lower:
            return response
    
    return DEFAULT_CHAT_RESPONSE


def get_dark_sky_locations(city):
    """Get stargazing locations for a city."""
    city_lower = city.lower().strip()
    
    # Check for exact or partial match
    for key in DARK_SKY_LOCATIONS:
        if key in city_lower or city_lower in key:
            return {
                "city": city,
                "locations": DARK_SKY_LOCATIONS[key],
                "tips": [
                    "Visit during new moon for darkest skies",
                    "Arrive early to let your eyes adjust (30 min)",
                    "Use red flashlight to preserve night vision",
                    "Check weather and air quality before driving",
                    "Download a stargazing app like Stellarium or SkySafari"
                ]
            }
    
    # Return default suggestions
    return {
        "city": city,
        "locations": DARK_SKY_LOCATIONS["default"],
        "tips": [
            "Visit darksky.org to find certified Dark Sky Places near you",
            "Generally, drive 50+ km from the city for better skies",
            "Higher elevation reduces atmospheric interference",
            "Avoid nights near full moon for best deep sky viewing"
        ],
        "note": f"Specific locations for '{city}' not in database. Try major cities or use these general guidelines."
    }


def get_events(count=6):
    """Get upcoming astronomy events."""
    return ASTRONOMY_EVENTS_2026[:count]


def get_seasonal_constellation_info():
    """Get constellation info for current season."""
    import datetime
    month = datetime.datetime.now().month
    
    if month in [12, 1, 2]:
        return CONSTELLATION_DATA["winter_north"]
    elif month in [3, 4, 5]:
        return CONSTELLATION_DATA["spring_north"]
    elif month in [6, 7, 8]:
        return CONSTELLATION_DATA["summer_north"]
    else:
        return CONSTELLATION_DATA["fall_north"]
