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

class SampleTreatmentType(str, Enum):
    in_vivo = "in_vivo"
    in_vitro = "in_vitro"
    not_applied = "not_applied"

class Replicate(str, Enum):
    # TODO: not sure about this
    patients = "patients"
    technical = "technical"

class ExperimentalOverview(BaseModel):
    title: str
    description: str
    experiment_type: str

class ExperimentVariablesControls(BaseModel):
    experimental_factor: str
    experimental_factor_value: str
    experimental_factor_units: str
    sample_treatment_type: SampleTreatmentType
    replicates: List[Replicate]
    quality_control: str

class ExperimentalDesign(BaseModel):
    experimental_overview: ExperimentalOverview
    experiment_variables_controls: ExperimentVariablesControls

class BiologicalSystem(BaseModel):
    organism: str
    tissue_cell_type: str
    qualifier: Qualifier
    value: str
    source: str
    experimental_design: ExperimentalDesign

class SequenceReadData(BaseModel):
    # TODO: no field for raw data
    quality_scores: str
    scale: str
    data_format: DataFormat

class ProcessedData(BaseModel):
    # TODO: no fields for actual data and gene expression matrix
    data_format_processed: DataFormatProcessed

class Contributor(BaseModel):
    # TODO: reconsider naming
    contributor: str
    contributor_orcid: str
    contributor_email: str
    institution: str

class ContactInformation(BaseModel):
    # TODO: reconsider naming
    author: str
    author_orcid: str # special for ORCID ID url
    author_email: str # speical for email
    institution: str
    contributors: List[Contributor]

class Link(BaseModel):
    # TODO: add more desriptive fields
    url: str # special for url

class GeneralInformation(BaseModel):
    study_summary: str
    sample_data_relationship: str
    contact_information: ContactInformation
    publication_information: str
    links: List[Link]

class ExperimentDataProcessingProtocols(BaseModel):
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

class Minseqe(BaseModel):
    # TODO: add all other missing fields from the paper
    # === 1. Biological System, Samples and Experimental Variables ===
    biological_system: BiologicalSystem
    
    # === 2. Sequence Read Data ===
    # TODO: add missing fields: Quality Scores ID, Data Format ID
    sequence_read_data: SequenceReadData
    
    # === 3. Processed Data ===
    # TODO: add missing fields: Data Format ID, Gene Expression Data Matrix ID
    processed_data: ProcessedData
    
    # === 4. General Information and Sample-Data Relationships ===
    # TODO: add all sample fields
    general_information: GeneralInformation
    
    # === 5. Experiment and Data Processing Protocols ===
    experiment_data_processing_protocols: ExperimentDataProcessingProtocols
    