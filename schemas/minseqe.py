from pydantic import BaseModel
from enum import Enum
from typing import List

class Qualifier(str, Enum):
    strain = "strain"
    age = "age"
    treatment = "treatment"

class DataFormat(str, Enum):
    fastq = "fastq"

class DataFormatProcessed(str, Enum):
    csv = "csv"
    xlsx = "xlsx"

class BiologicalSystem(BaseModel):
    organism: str
    tissue_cell_type: str
    qualifier: Qualifier
    value: str
    source: str
    experimental_factors: str
    experimental_factor_values: str

class SequenceReadData(BaseModel):
    # no field for raw data
    quality_scores: str
    scale: str
    data_format: DataFormat

class ProcessedData(BaseModel):
    # no fields for actual data and gene expression matrix
    data_format_processed: DataFormatProcessed

class Contributor(BaseModel):
    contributor: str
    contributor_orcid: str
    contributor_email: str
    institution: str

class ContactInformation(BaseModel):
    author: str
    author_orcid: str # special for ORCID ID url
    author_email: str # speical for email
    institution: str
    contributors: List[Contributor]

class GeneralInformation(BaseModel):
    study_summary: str
    sample_data_relationship: str
    contact_information: ContactInformation
    publication_information: str

class Minseqe(BaseModel):
    # === 1. Biological System, Samples and Experimental Variables ===
    biological_system: BiologicalSystem
    
    # === 2. Sequence Read Data ===
    sequence_read_data: SequenceReadData
    
    # === 3. Processed Data ===
    processed_data: ProcessedData
    
    # === 4. General Information and Sample-Data Relationships ===
    general_information: GeneralInformation
    
    # === 5. Experiment and Data Processing Protocols ===
    sample_processing_protocols: str
    extraction: str
    purification: str
    preparation: str
    sequencing_technology: str
    library_preparation_method: str
    sequencing_chemistry: str
    labelling_methodology: str
    amplification_methodology: str
    read_mapping_alignment_methods: str
    