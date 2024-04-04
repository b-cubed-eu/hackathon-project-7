from rocrate.rocrate import ROCrate
from rocrate.model import DataEntity, ContextEntity, Person
import datetime

crate = ROCrate()

crate.root_dataset["identifier"] = "#RoHubDOI"  # TODO: Add DOI
crate.name = "Example RO-Crate for a Data Cube"  # TODO: Change name
crate.description = "This is an RO-Crate metadata file developed for the B-Cubed Hackathon (Project 7 - ...) as an example."  # TODO: Change description
crate.root_dataset["dateCreated"] = str(datetime.date.today())
crate.keywords = [
    "hackathon",
    "data cubes",
    "biodiversity"
]  # TODO: update keywords

# Data Entities (datasets, scripts...)
bcubedDataset = crate.add_dataset(source="", properties={

})
gbifDataset = crate.add(DataEntity(crate, identifier="#GBIF-DOI", properties={
    "@type": "Dataset",
    "name": "",
    "description": ""
}))
crate.root_dataset.append_to("relatedIdentifiers", [gbifDataset, ])  # TODO: Complete datasets

# Contextual Entities (authors, organisations, activities...)
authorJulian = crate.add(Person(crate, identifier="http://orcid.org/0000-0003-0401-5122", properties={
    "name": "Julian Lopez Gordillo",
    "affiliation": {"@id": "https://ror.org/0566bfb96"}
}))
# authorName = crate.add(Person(crate, identifier="#ORCiD", properties={
#     "name": "",
#     "affiliation": {"@id": "#ROR"}
# }))
crate.root_dataset.append_to("creator", [authorJulian, ])  # TODO: Complete authors

# Organisations
eLTER = crate.add(ContextEntity(crate, "https://elter-ri.eu/", properties={
    "@type": "Organization",
    "name": "eLTER",
    "url": "https://elter-ri.eu/",
}))
Naturalis = crate.add(ContextEntity(crate, "https://ror.org/0566bfb96", properties={
    "@type": "Organization",
    "name": "Naturalis Biodiversity Center",
    "url": "http://www.naturalis.nl/"
}))
# orgName = crate.add(ContextEntity(crate, "#ROR (or URL)", properties={
#         "@type": "Organization",
#         "name": "",
#         "url": ""
#     }))
# crate.root_dataset.append_to("organization", [eLTER, Naturalis])

# Other
hackathon = crate.add(ContextEntity(crate, "#bcubed_hackathon", properties={
    "@type": "Hackathon",
    "name": "B-Cubed Hackathon",
    "location": "Brussels, Belgium",
    "startDate": "2024-04-02",
    "endDate": "2024-04-05"
}))
crate.root_dataset.append_to("publisher", hackathon)

licence = crate.add(ContextEntity(crate, identifier="https://creativecommons.org/licenses/by/4.0/", properties={
    "@type": "CreativeWork",
    "name": "Creative Commons Attribution 4.0 International",
    "description": "You are free to:\nShare — copy and redistribute the material in any medium or format for any purpose, even commercially.\nAdapt — remix, transform, and build upon the material for any purpose, even commercially.\nThe licensor cannot revoke these freedoms as long as you follow the license terms."
}))
crate.root_dataset.append_to("license", licence)

# Write file
crate.write("bcubed7_ro-crate")
# crate.write_zip("bcubed7_ro-crate")

