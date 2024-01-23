SQ_FT = "sq ft"
SQ_M = "sq m"

PROPERTY_SIZES = [SQ_FT, SQ_M]
PROPERTY_SIZE_CHOICES = ((SQ_FT, "sq ft"), (SQ_M, "sq m"))

# If the property is new, existing or other
NEW_BUILD = "NEW_BUILD"
EXISTING_BUILD = "EXISTING_BUILD"
OTHER = "OTHER"
BUILD_TYPE_CHOICES = (
    (NEW_BUILD, "New Build"),
    (EXISTING_BUILD, "Existing Build"),
    (OTHER, "Other"),
)

# If the property is commercial, residential or retail
COMMERCIAL = "COMMERCIAL"
RESIDENTIAL = "RESIDENTIAL"
RETAIL = "RETAIL"
USE_TYPE_CHOICES = (
    (COMMERCIAL, "Commercial"),
    (RESIDENTIAL, "Residential"),
    (RETAIL, "Retail"),
)
