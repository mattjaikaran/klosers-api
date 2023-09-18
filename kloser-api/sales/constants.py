QUARTER_CHOICES = ((1, "Q1"), (2, "Q2"), (3, "Q3"), (4, "Q4"))

# Average Deal Size
FIVE_TEN_K = "FIVE_TEN_K"
TEN_TWENTY_K = "TEN_TWENTY_K"
TWENTY_THIRTY_K = "TWENTY_THIRTY_K"
THIRTY_FORTY_K = "THIRTY_FORTY_K"
FORTY_FIFTY_K = "FORTY_FIFTY_K"
FIFTY_SIXTY_K = "FIFTY_SIXTY_K"
SIXTY_SEVENTY_K = "SIXTY_SEVENTY_K"
SEVENTY_EIGHTY_K = "SEVENTY_EIGHTY_K"
EIGHTY_NINETY_K = "EIGHTY_NINETY_K"
NINETY_HUNDRED_K = "NINETY_HUNDRED_K"
OVER_HUNDRED_K = "OVER_HUNDRED_K"

DEAL_SIZE_CHOICES = (
    (FIVE_TEN_K, "5k - 10k"),
    (TEN_TWENTY_K, "10k - 20k"),
    (TWENTY_THIRTY_K, "20k - 30k"),
    (THIRTY_FORTY_K, "30k - 40k"),
    (FORTY_FIFTY_K, "40k - 50k"),
    (FIFTY_SIXTY_K, "50k - 60k"),
    (SIXTY_SEVENTY_K, "60k - 70k"),
    (SEVENTY_EIGHTY_K, "70k - 80k"),
    (EIGHTY_NINETY_K, "80k - 90k"),
    (NINETY_HUNDRED_K, "90k - 100k"),
    (OVER_HUNDRED_K, "> 100k"),
)

# Market Segment
CONSUMER_DIRECT = "CONSUMER"
SMALL_BUSINESS = "SMALL_BUSINESS"
MID_MARKET = "MID_MARKET"
ENTERPRISE = "ENTERPRISE"
BUSINESS_DEVELOPMENT = "BUSINESS_DEVELOPMENT"

MARKET_CHOICES = (
    (CONSUMER_DIRECT, "Consumer Direct Sales"),
    (SMALL_BUSINESS, "SMB (Small Business) Sales"),
    (MID_MARKET, "Mid-Market Sales"),
    (ENTERPRISE, "Enterprise Sales"),
    (BUSINESS_DEVELOPMENT, "Business Development"),
)

# Job Titles (GTM)
CRO = "Chief Revenue Officer (CRO)"
CMO = "Chief Marketing Officer (CMO)"
VP_SALES = "VP of Sales"
HEAD_OF_SALES = "Head of Sales"
ACCOUNT_EXEC = "Account Executive"
SR_ACCOUNT_EXEC = "Sr. Account Executive"
STRATEGIC_ACCOUNT_EXEC = "Strategic Account Executive"
MIDMARKET_ACCOUNT_EXEC = "Mid Market Account Executive"
ENTERPRISE_ACCOUNT_EXEC = "Enterprise Account Executive"
DIRECTOR_MARKETING = "Director of Marketing"
SR_DIRECTOR_MARKETING = "Sr. Director of Marketing"
PRODUCT_MARKETING_MANAGER = "Product Marketing Manager"
MARKET_RESEARCH_ANALYST = "Market Research Analyst"
SALES_MANAGER = "Sales Manager"
SALES_DEV_REP = "Sales Development Representative"
BIZ_DEV_REP = "Business Development Representative"
BIZ_DEV_MANAGER = "Business Development Manager"
BRAND_MANAGER = "Brand Manager"
MARKETING_COORDINATOR = "Marketing Coordinator"
CONTENT_STRATEGIST = "Content Strategist"
CUSTOMER_SUCCESS_MANAGER = "Customer Success Manager"
SR_CUSTOMER_SUCCESS_MANAGER = "Sr. Customer Success Manager"
MARKET_STRATEGIST = "Market Strategist"
CHANNEL_SALES_MANAGER = "Channel Sales Manager"
PARTNER_MANAGER = "Partner Manager"
SALES_ENABLEMENT_SPECIALIST = "Sales Enablement Specialist"
CUSTOMER_EXPERIENCE_MANAGER = "Customer Experience Manager"
DATA_ANALYST = "Data Analyst"
USER_ACQ_MANAGER = "User Acquisition Manager"
DEMAND_GENERATION_SPECIALIST = "Demand Generation Specialist"

JOB_TITLE_CHOICES = (
    (CRO, "Chief Revenue Officer (CRO)"),
    (CMO, "Chief Marketing Officer (CMO)"),
    (VP_SALES, "VP of Sales"),
    (HEAD_OF_SALES, "Head of Sales"),
    (ACCOUNT_EXEC, "Account Executive"),
    (SR_ACCOUNT_EXEC, "Sr. Account Executive"),
    (STRATEGIC_ACCOUNT_EXEC, "Strategic Account Executive"),
    (MIDMARKET_ACCOUNT_EXEC, "Mid Market Account Executive"),
    (ENTERPRISE_ACCOUNT_EXEC, "Enterprise Account Executive"),
    (DIRECTOR_MARKETING, "Director of Marketing"),
    (SR_DIRECTOR_MARKETING, "Sr. Director of Marketing"),
    (PRODUCT_MARKETING_MANAGER, "Product Marketing Manager"),
    (MARKET_RESEARCH_ANALYST, "Market Research Analyst"),
    (SALES_MANAGER, "Sales Manager"),
    (SALES_DEV_REP, "Sales Development Representative"),
    (BIZ_DEV_REP, "Business Development Representative"),
    (BIZ_DEV_MANAGER, "Business Development Manager"),
    (BRAND_MANAGER, "Brand Manager"),
    (MARKETING_COORDINATOR, "Marketing Coordinator"),
    (CONTENT_STRATEGIST, "Content Strategist"),
    (CUSTOMER_SUCCESS_MANAGER, "Customer Success Manager"),
    (SR_CUSTOMER_SUCCESS_MANAGER, "Sr. Customer Success Manager"),
    (MARKET_STRATEGIST, "Market Strategist"),
    (CHANNEL_SALES_MANAGER, "Channel Sales Manager"),
    (PARTNER_MANAGER, "Partner Manager"),
    (SALES_ENABLEMENT_SPECIALIST, "Sales Enablement Specialist"),
    (CUSTOMER_EXPERIENCE_MANAGER, "Customer Experience Manager"),
    (DATA_ANALYST, "Data Analyst"),
    (USER_ACQ_MANAGER, "User Acquisition Manager"),
    (DEMAND_GENERATION_SPECIALIST, "Demand Generation Specialist"),
)


SALES_CYCLE_CHOICES = (
    ("<30", "< 30 Days"),
    ("30", "30 Days"),
    ("45", "45 Days"),
    ("60", "60 Days"),
    ("90", "90 Days"),
    ("120", "120 Days"),
    (">120", "> 120 Days"),
)

INDUSTRY_CHOICES = (
    ("IT", "Information Technology (IT) Services"),
    ("CYBERSECURITY", "Cybersecurity"),
    ("SAAS", "Software as a Service (SaaS)"),
    ("AI_ML", "Artificial Intelligence (AI) and Machine Learning (ML)"),
    ("HARDWARE", "Hardware"),
    ("TELECOMMUNICATIONS", "Telecommunications"),
    ("E_COMMERCE", "E-commerce Platforms"),
    ("EDTECH", "EdTech"),
    ("FINTECH", "FinTech"),
    ("HEALTHTECH", "HealthTech/MedTech"),
    ("ERP", "Enterprise Resource Planning (ERP) Systems"),
    ("SOCIAL_MEDIA", "Social Media Platforms"),
    ("BIG_DATA", "Big Data and Analytics"),
    ("IOT", "Internet of Things (IoT)"),
    ("AR_VR", "Augmented Reality (AR)/Virtual Reality (VR)"),
    ("BLOCKCHAIN", "Blockchain and Cryptocurrency"),
    ("CLEANTECH", "CleanTech"),
    ("CLOUD_SERVICES", "Cloud Services"),
    ("GAMING", "Gaming"),
    ("5G", "5G Technology"),
    ("ADTECH", "AdTech"),
    ("PHARMACEUTICAL", "Pharmaceutical"),
    ("MEDICAL_DEVICES", "Medical Devices"),
    ("AUTOMOTIVE", "Automotive"),
    ("REAL_ESTATE", "Real Estate"),
    ("RETAIL", "Retail"),
    ("WHOLESALE_TRADE", "Wholesale Trade"),
    ("INSURANCE", "Insurance"),
    ("FINANCIAL_SERVICES", "Financial Services"),
    ("CPG", "Consumer Packaged Goods (CPG)"),
    ("FOOD_BEVERAGE", "Food and Beverage"),
    ("HOSPITALITY", "Hospitality"),
    ("TRAVEL_TOURISM", "Travel and Tourism"),
    ("SPORTS_ENTERTAINMENT", "Sports and Entertainment"),
    ("PUBLISHING_MEDIA", "Publishing and Media"),
    ("ADVERTISING_MARKETING", "Advertising and Marketing"),
    ("APPAREL_FASHION", "Apparel and Fashion"),
    ("FURNITURE_DECOR", "Furniture and Home Decor"),
    ("CONSTRUCTION", "Construction and Building Materials"),
    ("INDUSTRIAL_MANUFACTURING", "Industrial and Manufacturing"),
    ("ENERGY_UTILITIES", "Energy and Utilities"),
    ("AEROSPACE_DEFENSE", "Aerospace and Defense"),
    ("AGRICULTURE", "Agriculture"),
    ("TRANSPORTATION_LOGISTICS", "Transportation and Logistics"),
    ("EDUCATION", "Education"),
    ("FITNESS_WELLNESS", "Fitness and Wellness"),
    ("PROFESSIONAL_SERVICES", "Professional Services"),
    ("NONPROFIT", "Nonprofit Sector"),
    ("COSMETICS_PERSONAL_CARE", "Cosmetics and Personal Care"),
    ("LUXURY_GOODS_JEWELRY", "Luxury Goods and Jewelry"),
    ("PET_PRODUCTS_SERVICES", "Pet Products and Services"),
    ("ENVIRONMENTAL_SERVICES", "Environmental Services"),
    ("WINE_SPIRITS", "Wine and Spirits"),
)
