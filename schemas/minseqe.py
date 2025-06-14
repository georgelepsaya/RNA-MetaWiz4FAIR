from pydantic import BaseModel, HttpUrl
from enum import Enum
from typing import List

# === Enumerations ===

class Qualifier(str, Enum):
    strain = "strain"
    age = "age"
    treatment = "treatment"

class DataFormatRaw(str, Enum):
    fastq = "fastq"
    fastq_gz = "fastq.gz"

class DataFormatProcessed(str, Enum):
    csv = "csv"
    tsv = "tsv"
    xlsx = "xlsx"

class SampleTreatmentType(str, Enum):
    in_vivo = "in_vivo"
    in_vitro = "in_vitro"
    not_applied = "not_applied"

class Replicate(str, Enum):
    # TODO: not sure about this
    patients = "patients"
    technical = "technical"

# === 1. Biological System, Samples and Experimental Variables ===

class ExperimentalOverview(BaseModel):
    title: str
    description: str
    experiment_type: str

class ExperimentalVariable(BaseModel):
    experimental_factor: str
    experimental_factor_value: str
    experimental_factor_units: str

class ExperimentVariablesControls(BaseModel):
    variables: List[ExperimentalVariable]
    sample_treatment_type: SampleTreatmentType
    replicates: List[Replicate]
    quality_control: str

class ExperimentalDesign(BaseModel):
    experimental_overview: ExperimentalOverview
    experiment_variables_controls: ExperimentVariablesControls

class BiologicalSystem(BaseModel):
    organism: str
    organism_id: str
    tissue_cell_type: str
    tissue_cell_type_id: str
    qualifier: Qualifier
    value: str
    source: str
    experimental_design: ExperimentalDesign

# === Sample Description ===

class Sample(BaseModel):
    sample_id: str
    organism: str
    organism_id: str
    tissue_type: str
    tissue_type_id: str
    cell_type: str
    cell_type_id: str
    qualifiers: List[Qualifier]
    qualifier_values: List[str]
    source: str

# === 2. Sequence Read Data ===

class SequenceReadData(BaseModel):
    raw_data_id: str  # ID for reference in the sample‑data relationship table
    raw_data: HttpUrl  # URL path to raw data
    quality_scores: str
    scale: str
    data_format: DataFormatRaw

# === 3. Processed Data ===

class ProcessedData(BaseModel):
    processed_data_id: str  # ID for reference in the sample‑data relationship table
    processed_data: HttpUrl  # URL path to processed data
    data_format_processed: DataFormatProcessed
    data_format_id: str # ID from Ontology
    gene_expression_matrix: HttpUrl  # URL path to the spreadsheet
    gene_expression_matrix_description: str
    gene_expression_matrix_id: str # ID from Ontology

# === 4. General Information and Sample‑Data Relationships ===

class Contributor(BaseModel):
    contributor: str
    orcid: str
    email: str
    institution: str

class ContactInformation(BaseModel):
    author: str
    orcid: str
    email: str
    institution: str
    contributors: List[Contributor]

class Link(BaseModel):
    # TODO: perhaps add more field, eg citation or date accessed
    url: HttpUrl
    description: str

class SampleDataRelationship(BaseModel):
    sample_id: str
    raw_data_id: str
    processed_data_id: str

class GeneralInformation(BaseModel):
    study_summary: str
    sample_data_relationships: List[SampleDataRelationship]
    contact_information: ContactInformation
    publication_information: str
    links: List[Link]

# === 5. Experimental and Data Processing Protocols ===

class DataProcessingMapping(BaseModel):
    read_mapping_alignment_methods: str
    alignment_methods: str
    data_filtering_quality_control_methods: str
    data_rejection_methods: str
    data_correction_methods: str
    data_smoothing_methods: str
    data_filtering_methods: str
    data_normalization_method: str
    data_analysis_tools_algorithms: str
    identifiers: str

class ExperimentDataProcessingProtocols(BaseModel):
    sample_processing_protocols: str
    extraction: str
    purification: str
    preparation: str
    sequencing_platform_technology: str
    library_preparation_method: str
    sequencing_chemistry: str
    labelling_methodology: str
    amplification_methodology: str
    data_processing_mapping: DataProcessingMapping

# === Top‑level MINSEQE Model ===

class Minseqe(BaseModel):
    # === 1. Biological System, Samples and Experimental Variables ===
    biological_system: BiologicalSystem
    samples: List[Sample]

    # === 2. Sequence Read Data ===
    sequence_read_data: List[SequenceReadData]

    # === 3. Processed Data ===
    processed_data: List[ProcessedData]

    # === 4. General Information and Sample‑Data Relationships ===
    general_information: GeneralInformation

    # === 5. Experimental and Data Processing Protocols ===
    experiment_data_processing_protocols: ExperimentDataProcessingProtocols
