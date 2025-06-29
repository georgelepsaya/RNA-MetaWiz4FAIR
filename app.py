import streamlit as st
from chain.agent import RNAMetadataAgent


def handle_help_button_click(field_name: str, field_description: str):
    """Handle help button clicks by automatically sending a prompt to the AI assistant"""
    prompt = f"Help me with the '{field_name}' field. {field_description}"
    
    # Add the user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get response from agent
    with st.spinner("Getting help..."):
        try:
            assistant_reply = st.session_state.agent.get_suggestion(
                user_input=prompt,
                current_metadata=st.session_state.metadata,
                chat_history=st.session_state.messages[:-1]
            )
            
            st.session_state.messages.append({
                "role": "assistant", 
                "content": assistant_reply
            })
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            st.session_state.messages.append({
                "role": "assistant", 
                "content": error_msg
            })
            st.error(f"Failed to get response: {str(e)}")


if "metadata" not in st.session_state:
    st.session_state.metadata = {}
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = RNAMetadataAgent()

st.set_page_config(layout="wide")
st.title("RNA MetaWiz")

st.warning(
    """
    This is a Demo of the RNA MetaWiz. You can:\n
    
    - Fill out the fields
    - Ask AI assistant for context-relevant help
    - Get real information from Ontology databases with one click\n
    
    You can also view the metadata being constructed. \n
    **Do NOT** use this as an actual tool for metadata annotation.
    Metadata fields are **NOT complete** and **there is NO validation** of them.\n
    **Your current session is NOT persisted**. \n
    We welcome your feedback. Feel free to open an issue on our GitHub repo or contact us at.
    """)


col1, col2 = st.columns([3, 1], gap="large")

with col1:
    # === 1. Biological System ===
    st.subheader("🧬 Biological System")
    
    with st.expander("Basic Organism Information"):

        st.markdown("**Organism**")
        st.caption("The name of the organism (e.g., Homo sapiens, Mus musculus).")
        if st.button("Help with Organism", icon="🤖", key="help_organism"):
            handle_help_button_click("Organism", "The name of the organism (e.g., Homo sapiens, Mus musculus).")
        st.text_input(
            "Organism",
            key="organism",
            label_visibility="collapsed"
        )

        st.markdown("**Organism ID**")
        st.caption("Taxonomy ID or database identifier for the organism (e.g., 9606 for human).")
        if st.button("Help with Organism ID", icon="🤖", key="help_organism_id"):
            handle_help_button_click("Organism ID", "Taxonomy ID or database identifier for the organism (e.g., 9606 for human).")
        st.text_input(
            "Organism ID", 
            key="organism_id",
            label_visibility="collapsed"
        )

        st.markdown("**Tissue / Cell type**")
        st.caption("The specific tissue or cell type used in the experiment.")
        if st.button("Help with Tissue / Cell type", icon="🤖", key="help_tissue_cell_type"):
            handle_help_button_click("Tissue / Cell type", "The specific tissue or cell type used in the experiment.")
        st.text_input(
            "Tissue / Cell type", 
            key="tissue_cell_type",
            label_visibility="collapsed"
        )

        st.markdown("**Tissue / Cell type ID**")
        st.caption("Ontology ID for the tissue or cell type (e.g., UBERON, CL).")
        if st.button("Help with Tissue / Cell type ID", icon="🤖", key="help_tissue_cell_type_id"):
            handle_help_button_click("Tissue / Cell type ID", "Ontology ID for the tissue or cell type (e.g., UBERON, CL).")
        st.text_input(
            "Tissue / Cell type ID", 
            key="tissue_cell_type_id",
            label_visibility="collapsed"
        )
        
        st.markdown("**Qualifier**")
        st.caption("Type of qualifier: strain (genetic variant), age (developmental stage), or treatment (experimental condition).")
        if st.button("Help with Qualifier", icon="🤖", key="help_qualifier"):
            handle_help_button_click("Qualifier", "Type of qualifier: strain (genetic variant), age (developmental stage), or treatment (experimental condition).")
        st.selectbox(
            "Qualifier",
            options=["strain", "age", "treatment"],
            key="qualifier",
            label_visibility="collapsed"
        )

        st.markdown("**Value**")
        st.caption("The specific value for the qualifier (e.g., 'C57BL/6J' for strain, '8 weeks' for age).")
        if st.button("Help with Value", icon="🤖", key="help_value"):
            handle_help_button_click("Value", "The specific value for the qualifier (e.g., 'C57BL/6J' for strain, '8 weeks' for age).")
        st.text_input(
            "Value", 
            key="value",
            label_visibility="collapsed"
        )

        st.markdown("**Source**")
        st.caption("Source or reference for the biological material.")
        if st.button("Help with Source", icon="🤖", key="help_source"):
            handle_help_button_click("Source", "Source or reference for the biological material.")
        st.text_input(
            "Source",
            key="source",
            label_visibility="collapsed"
        )
        
    # === Experimental Design ===
    with st.expander("Experimental Design"):
        st.markdown("**Experiment Title**")
        st.caption("A concise title describing the experiment.")
        if st.button("Help with Experiment Title", icon="🤖", key="help_experiment_title"):
            handle_help_button_click("Experiment Title", "A concise title describing the experiment.")
        st.text_input(
            "Experiment Title",
            key="experiment_title",
            label_visibility="collapsed"
        )

        st.markdown("**Experiment Description**")
        st.caption("A detailed description of the experimental setup and objectives.")
        if st.button("Help with Experiment Description", icon="🤖", key="help_experiment_description"):
            handle_help_button_click("Experiment Description", "A detailed description of the experimental setup and objectives.")
        st.text_area(
            "Experiment Description",
            key="experiment_description",
            label_visibility="collapsed"
        )

        st.markdown("**Experiment Type**")
        st.caption("Type of RNA-seq experiment (e.g., differential expression, time course)")
        if st.button("Help with Experiment Type", icon="🤖", key="help_experiment_type"):
            handle_help_button_click("Experiment Type", "Type of RNA-seq experiment (e.g., differential expression, time course)")
        st.text_input(
            "Experiment Type",
            key="experiment_type",
            label_visibility="collapsed"
        )
    
        # Experimental Variables
        st.markdown("**Experimental Variables**")

        st.markdown("**Experimental Factor**")
        st.caption("The main experimental variable being tested (e.g., drug treatment, time point)")
        if st.button("Help with Experimental Factor", icon="🤖", key="help_experimental_factor"):
            handle_help_button_click("Experimental Factor", "The main experimental variable being tested (e.g., drug treatment, time point)")
        st.text_input(
            "Experimental Factor",
            key="experimental_factor",
            label_visibility="collapsed"
        )

        st.markdown("**Experimental Factor Value**")
        st.caption("The specific value or condition of the experimental factor")
        if st.button("Help with Experimental Factor Value", icon="🤖", key="help_experimental_factor_value"):
            handle_help_button_click("Experimental Factor Value", "The specific value or condition of the experimental factor")
        st.text_input(
            "Experimental Factor Value",
            key="experimental_factor_value",
            label_visibility="collapsed"
        )

        st.markdown("**Experimental Factor Units**")
        st.caption("Units for the experimental factor value (e.g., mg/kg, hours)")
        if st.button("Help with Experimental Factor Units", icon="🤖", key="help_experimental_factor_units"):
            handle_help_button_click("Experimental Factor Units", "Units for the experimental factor value (e.g., mg/kg, hours)")
        st.text_input(
            "Experimental Factor Units",
            key="experimental_factor_units",
            label_visibility="collapsed"
        )

        st.markdown("**Sample Treatment Type**")
        st.caption("Whether the experiment was conducted in living organisms (in_vivo), in culture (in_vitro), or no treatment applied")
        if st.button("Help with Sample Treatment Type", icon="🤖", key="help_sample_treatment_type"):
            handle_help_button_click("Sample Treatment Type", "Whether the experiment was conducted in living organisms (in_vivo), in culture (in_vitro), or no treatment applied")
        st.selectbox(
            "Sample Treatment Type",
            options=["in_vivo", "in_vitro", "not_applied"],
            key="sample_treatment_type",
            label_visibility="collapsed"
        )

        st.markdown("**Replicates**")
        st.caption("Types of replicates used: patients (biological replicates) or technical (technical replicates)")
        if st.button("Help with Replicates", icon="🤖", key="help_replicates"):
            handle_help_button_click("Replicates", "Types of replicates used: patients (biological replicates) or technical (technical replicates)")
        st.multiselect(
            "Replicates",
            options=["patients", "technical"],
            key="replicates",
            label_visibility="collapsed"
        )

        st.markdown("**Quality Control**")
        st.caption("Description of quality control measures applied to samples")
        if st.button("Help with Quality Control", icon="🤖", key="help_quality_control"):
            handle_help_button_click("Quality Control", "Description of quality control measures applied to samples")
        st.text_area(
            "Quality Control",
            key="quality_control",
            label_visibility="collapsed"
        )
    
    # === 2. Sample Information ===
    st.subheader("🧪 Sample Information")

    with st.expander("Samples"):
        st.markdown("**Sample ID**")
        st.caption("Unique identifier for the sample")
        if st.button("Help with Sample ID", icon="🤖", key="help_sample_id"):
            handle_help_button_click("Sample ID", "Unique identifier for the sample")
        st.text_input(
            "Sample ID",
            key="sample_id",
            label_visibility="collapsed"
        )

        st.markdown("**Sample Organism**")
        st.caption("Organism for this specific sample (if different from main organism)")
        if st.button("Help with Sample Organism", icon="🤖", key="help_sample_organism"):
            handle_help_button_click("Sample Organism", "Organism for this specific sample (if different from main organism)")
        st.text_input(
            "Sample Organism",
            key="sample_organism",
            label_visibility="collapsed"
        )

        st.markdown("**Sample Organism ID**")
        st.caption("Taxonomy ID for the sample organism")
        if st.button("Help with Sample Organism ID", icon="🤖", key="help_sample_organism_id"):
            handle_help_button_click("Sample Organism ID", "Taxonomy ID for the sample organism")
        st.text_input(
            "Sample Organism ID",
            key="sample_organism_id",
            label_visibility="collapsed"
        )

        st.markdown("**Tissue Type**")
        st.caption("Tissue type for this sample")
        if st.button("Help with Tissue Type", icon="🤖", key="help_tissue_type"):
            handle_help_button_click("Tissue Type", "Tissue type for this sample")
        st.text_input(
            "Tissue Type",
            key="tissue_type",
            label_visibility="collapsed"
        )

        st.markdown("**Tissue Type ID**")
        st.caption("Ontology ID for the tissue type")
        if st.button("Help with Tissue Type ID", icon="🤖", key="help_tissue_type_id"):
            handle_help_button_click("Tissue Type ID", "Ontology ID for the tissue type")
        st.text_input(
            "Tissue Type ID",
            key="tissue_type_id",
            label_visibility="collapsed"
        )

        st.markdown("**Cell Type**")
        st.caption("Specific cell type for this sample")
        if st.button("Help with Cell Type", icon="🤖", key="help_cell_type"):
            handle_help_button_click("Cell Type", "Specific cell type for this sample")
        st.text_input(
            "Cell Type",
            key="cell_type",
            label_visibility="collapsed"
        )

        st.markdown("**Cell Type ID**")
        st.caption("Ontology ID for the cell type")
        if st.button("Help with Cell Type ID", icon="🤖", key="help_cell_type_id"):
            handle_help_button_click("Cell Type ID", "Ontology ID for the cell type")
        st.text_input(
            "Cell Type ID",
            key="cell_type_id",
            label_visibility="collapsed"
        )

        st.markdown("**Sample Source**")
        st.caption("Source or origin of this specific sample")
        if st.button("Help with Sample Source", icon="🤖", key="help_sample_source"):
            handle_help_button_click("Sample Source", "Source or origin of this specific sample")
        st.text_input(
            "Sample Source",
            key="sample_source",
            label_visibility="collapsed"
        )

    
    # === 3. Sequence Read Data ===
    st.subheader("📊 Sequence Read Data")

    with st.expander("Raw Data"):
        st.markdown("**Raw Data ID**")
        st.caption("Unique identifier for the raw sequencing data")
        if st.button("Help with Raw Data ID", icon="🤖", key="help_raw_data_id"):
            handle_help_button_click("Raw Data ID", "Unique identifier for the raw sequencing data")
        st.text_input(
            "Raw Data ID",
            key="raw_data_id",
            label_visibility="collapsed"
        )

        st.markdown("**Raw Data URL**")
        st.caption("URL or file path to the raw sequencing data files")
        if st.button("Help with Raw Data URL", icon="🤖", key="help_raw_data_url"):
            handle_help_button_click("Raw Data URL", "URL or file path to the raw sequencing data files")
        st.text_input(
            "Raw Data URL",
            key="raw_data_url",
            label_visibility="collapsed"
        )

        st.markdown("**Quality Scores**")
        st.caption("Description of quality score format (e.g., Phred+33, Phred+64)")
        if st.button("Help with Quality Scores", icon="🤖", key="help_quality_scores"):
            handle_help_button_click("Quality Scores", "Description of quality score format (e.g., Phred+33, Phred+64)")
        st.text_input(
            "Quality Scores",
            key="quality_scores",
            label_visibility="collapsed"
        )

        st.markdown("**Scale**")
        st.caption("Scale used for quality scores")
        if st.button("Help with Scale", icon="🤖", key="help_scale"):
            handle_help_button_click("Scale", "Scale used for quality scores")
        st.text_input(
            "Scale",
            key="scale",
            label_visibility="collapsed"
        )

        st.markdown("**Data Format**")
        st.caption("Format of the raw sequencing data files")
        if st.button("Help with Data Format", icon="🤖", key="help_data_format"):
            handle_help_button_click("Data Format", "Format of the raw sequencing data files")
        st.selectbox(
            "Data Format",
            options=["fastq", "fastq.gz"],
            key="data_format",
            label_visibility="collapsed"
        )
    
    # === 4. Processed Data ===
    st.subheader("🔧 Processed Data")

    with st.expander("Processed Data"):
        st.markdown("**Processed Data ID**")
        st.caption("Unique identifier for the processed data")
        if st.button("Help with Processed Data ID", icon="🤖", key="help_processed_data_id"):
            handle_help_button_click("Processed Data ID", "Unique identifier for the processed data")
        st.text_input(
            "Processed Data ID",
            key="processed_data_id",
            label_visibility="collapsed"
        )

        st.markdown("**Processed Data URL**")
        st.caption("URL or file path to the processed data files")
        if st.button("Help with Processed Data URL", icon="🤖", key="help_processed_data_url"):
            handle_help_button_click("Processed Data URL", "URL or file path to the processed data files")
        st.text_input(
            "Processed Data URL",
            key="processed_data_url",
            label_visibility="collapsed"
        )

        st.markdown("**Processed Data Format**")
        st.caption("Format of the processed data files")
        if st.button("Help with Processed Data Format", icon="🤖", key="help_data_format_processed"):
            handle_help_button_click("Processed Data Format", "Format of the processed data files")
        st.selectbox(
            "Processed Data Format",
            options=["csv", "tsv", "xlsx"],
            key="data_format_processed",
            label_visibility="collapsed"
        )

        st.markdown("**Data Format ID**")
        st.caption("Ontology ID for the data format")
        if st.button("Help with Data Format ID", icon="🤖", key="help_data_format_id"):
            handle_help_button_click("Data Format ID", "Ontology ID for the data format")
        st.text_input(
            "Data Format ID",
            key="data_format_id",
            label_visibility="collapsed"
        )

        st.markdown("**Gene Expression Matrix URL**")
        st.caption("URL or file path to the gene expression matrix")
        if st.button("Help with Gene Expression Matrix URL", icon="🤖", key="help_gene_expression_matrix_url"):
            handle_help_button_click("Gene Expression Matrix URL", "URL or file path to the gene expression matrix")
        st.text_input(
            "Gene Expression Matrix URL",
            key="gene_expression_matrix_url",
            label_visibility="collapsed"
        )

        st.markdown("**Gene Expression Matrix Description**")
        st.caption("Description of the gene expression matrix content and structure")
        if st.button("Help with Gene Expression Matrix Description", icon="🤖", key="help_gene_expression_matrix_description"):
            handle_help_button_click("Gene Expression Matrix Description", "Description of the gene expression matrix content and structure")
        st.text_area(
            "Gene Expression Matrix Description",
            key="gene_expression_matrix_description",
            label_visibility="collapsed"
        )

        st.markdown("**Gene Expression Matrix ID**")
        st.caption("Ontology ID for the gene expression matrix")
        if st.button("Help with Gene Expression Matrix ID", icon="🤖", key="help_gene_expression_matrix_id"):
            handle_help_button_click("Gene Expression Matrix ID", "Ontology ID for the gene expression matrix")
        st.text_input(
            "Gene Expression Matrix ID",
            key="gene_expression_matrix_id",
            label_visibility="collapsed"
        )
    
    # === 5. General Information ===
    st.subheader("📋 General Information")

    with st.expander("General Information"):
        st.markdown("**Study Summary**")
        st.caption("Overall summary of the study objectives and findings")
        if st.button("Help with Study Summary", icon="🤖", key="help_study_summary"):
            handle_help_button_click("Study Summary", "Overall summary of the study objectives and findings")
        st.text_area(
            "Study Summary",
            key="study_summary",
            label_visibility="collapsed"
        )

        st.markdown("**Contact Information**")
        
        st.markdown("**Author**")
        st.caption("Primary author of the study")
        if st.button("Help with Author", icon="🤖", key="help_author"):
            handle_help_button_click("Author", "Primary author of the study")
        st.text_input(
            "Author",
            key="author",
            label_visibility="collapsed"
        )

        st.markdown("**Author ORCID**")
        st.caption("ORCID identifier for the primary author")
        if st.button("Help with Author ORCID", icon="🤖", key="help_author_orcid"):
            handle_help_button_click("Author ORCID", "ORCID identifier for the primary author")
        st.text_input(
            "Author ORCID",
            key="author_orcid",
            label_visibility="collapsed"
        )

        st.markdown("**Author Email**")
        st.caption("Email address of the primary author")
        if st.button("Help with Author Email", icon="🤖", key="help_author_email"):
            handle_help_button_click("Author Email", "Email address of the primary author")
        st.text_input(
            "Author Email",
            key="author_email",
            label_visibility="collapsed"
        )

        st.markdown("**Institution**")
        st.caption("Institution where the research was conducted")
        if st.button("Help with Institution", icon="🤖", key="help_institution"):
            handle_help_button_click("Institution", "Institution where the research was conducted")
        st.text_input(
            "Institution",
            key="institution",
            label_visibility="collapsed"
        )

        st.markdown("**Publication Information**")
        st.caption("Citation or publication details for this study")
        if st.button("Help with Publication Information", icon="🤖", key="help_publication_information"):
            handle_help_button_click("Publication Information", "Citation or publication details for this study")
        st.text_area(
            "Publication Information",
            key="publication_information",
            label_visibility="collapsed"
        )

        st.markdown("**Links**")
        st.caption("Additional links to related resources")
        if st.button("Help with Links", icon="🤖", key="help_links"):
            handle_help_button_click("Links", "Additional links to related resources")
        st.text_input(
            "Links",
            key="links",
            label_visibility="collapsed"
        )
    
    # === 6. Experimental Protocols ===
    st.subheader("🔬 Experimental Protocols")

    with st.expander("Experimental Protocols"):

        st.markdown("**Sample Processing Protocols**")
        st.caption("Detailed protocols for sample collection and processing")
        if st.button("Help with Sample Processing Protocols", icon="🤖", key="help_sample_processing_protocols"):
            handle_help_button_click("Sample Processing Protocols", "Detailed protocols for sample collection and processing")
        st.text_input(
            "Sample Processing Protocols",
            key="sample_processing_protocols",
            label_visibility="collapsed"
        )

        st.markdown("**Extraction Protocol**")
        st.caption("RNA extraction protocol used")
        if st.button("Help with Extraction Protocol", icon="🤖", key="help_extraction"):
            handle_help_button_click("Extraction Protocol", "RNA extraction protocol used")
        st.text_area(
            "Extraction Protocol",
            key="extraction",
            label_visibility="collapsed"
        )

        st.markdown("**Purification Protocol**")
        st.caption("RNA purification protocol used")
        if st.button("Help with Purification Protocol", icon="🤖", key="help_purification"):
            handle_help_button_click("Purification Protocol", "RNA purification protocol used")
        st.text_area(
            "Purification Protocol",
            key="purification",
            label_visibility="collapsed"
        )

        st.markdown("**Preparation Protocol**")
        st.caption("Sample preparation protocol for sequencing")
        if st.button("Help with Preparation Protocol", icon="🤖", key="help_preparation"):
            handle_help_button_click("Preparation Protocol", "Sample preparation protocol for sequencing")
        st.text_area(
            "Preparation Protocol",
            key="preparation",
            label_visibility="collapsed"
        )

        st.markdown("**Sequencing Platform/Technology**")
        st.caption("Sequencing platform and technology used (e.g., Illumina NovaSeq, Oxford Nanopore)")
        if st.button("Help with Sequencing Platform/Technology", icon="🤖", key="help_sequencing_platform_technology"):
            handle_help_button_click("Sequencing Platform/Technology", "Sequencing platform and technology used (e.g., Illumina NovaSeq, Oxford Nanopore)")
        st.text_input(
            "Sequencing Platform/Technology",
            key="sequencing_platform_technology",
            label_visibility="collapsed"
        )

        st.markdown("**Library Preparation Method**")
        st.caption("Method used for library preparation")
        if st.button("Help with Library Preparation Method", icon="🤖", key="help_library_preparation_method"):
            handle_help_button_click("Library Preparation Method", "Method used for library preparation")
        st.text_area(
            "Library Preparation Method",
            key="library_preparation_method",
            label_visibility="collapsed"
        )

        st.markdown("**Sequencing Chemistry**")
        st.caption("Sequencing chemistry version used")
        if st.button("Help with Sequencing Chemistry", icon="🤖", key="help_sequencing_chemistry"):
            handle_help_button_click("Sequencing Chemistry", "Sequencing chemistry version used")
        st.text_input(
            "Sequencing Chemistry",
            key="sequencing_chemistry",
            label_visibility="collapsed"
        )

        st.markdown("**Labelling Methodology**")
        st.caption("Method used for sample labelling if applicable")
        if st.button("Help with Labelling Methodology", icon="🤖", key="help_labelling_methodology"):
            handle_help_button_click("Labelling Methodology", "Method used for sample labelling if applicable")
        st.text_area(
            "Labelling Methodology",
            key="labelling_methodology",
            label_visibility="collapsed"
        )

        st.markdown("**Amplification Methodology**")
        st.caption("Amplification method used if applicable")
        if st.button("Help with Amplification Methodology", icon="🤖", key="help_amplification_methodology"):
            handle_help_button_click("Amplification Methodology", "Amplification method used if applicable")
        st.text_area(
            "Amplification Methodology",
            key="amplification_methodology",
            label_visibility="collapsed"
        )
    
    with st.expander("Data Processing"):
        st.markdown("**Data Processing Methods**")

        st.markdown("**Read Mapping/Alignment Methods**")
        st.caption("Methods used for read mapping and alignment")
        if st.button("Help with Read Mapping/Alignment Methods", icon="🤖", key="help_read_mapping_alignment_methods"):
            handle_help_button_click("Read Mapping/Alignment Methods", "Methods used for read mapping and alignment")
        st.text_area(
            "Read Mapping/Alignment Methods",
            key="read_mapping_alignment_methods",
            label_visibility="collapsed"
        )

        st.markdown("**Alignment Methods**")
        st.caption("Specific alignment algorithms and parameters used")
        if st.button("Help with Alignment Methods", icon="🤖", key="help_alignment_methods"):
            handle_help_button_click("Alignment Methods", "Specific alignment algorithms and parameters used")
        st.text_area(
            "Alignment Methods",
            key="alignment_methods",
            label_visibility="collapsed"
        )

        st.markdown("**Data Filtering/Quality Control Methods**")
        st.caption("Methods used for data filtering and quality control")
        if st.button("Help with Data Filtering/Quality Control Methods", icon="🤖", key="help_data_filtering_quality_control_methods"):
            handle_help_button_click("Data Filtering/Quality Control Methods", "Methods used for data filtering and quality control")
        st.text_area(
            "Data Filtering/Quality Control Methods",
            key="data_filtering_quality_control_methods",
            label_visibility="collapsed"
        )

        st.markdown("**Data Rejection Methods**")
        st.caption("Criteria and methods for rejecting low-quality data")
        if st.button("Help with Data Rejection Methods", icon="🤖", key="help_data_rejection_methods"):
            handle_help_button_click("Data Rejection Methods", "Criteria and methods for rejecting low-quality data")
        st.text_area(
            "Data Rejection Methods",
            key="data_rejection_methods",
            label_visibility="collapsed"
        )

        st.markdown("**Data Correction Methods**")
        st.caption("Methods used for data correction if applicable")
        if st.button("Help with Data Correction Methods", icon="🤖", key="help_data_correction_methods"):
            handle_help_button_click("Data Correction Methods", "Methods used for data correction if applicable")
        st.text_area(
            "Data Correction Methods",
            key="data_correction_methods",
            label_visibility="collapsed"
        )

        st.markdown("**Data Smoothing Methods**")
        st.caption("Methods used for data smoothing if applicable")
        if st.button("Help with Data Smoothing Methods", icon="🤖", key="help_data_smoothing_methods"):
            handle_help_button_click("Data Smoothing Methods", "Methods used for data smoothing if applicable")
        st.text_area(
            "Data Smoothing Methods",
            key="data_smoothing_methods",
            label_visibility="collapsed"
        )

        st.markdown("**Data Filtering Methods**")
        st.caption("Additional data filtering methods applied")
        if st.button("Help with Data Filtering Methods", icon="🤖", key="help_data_filtering_methods"):
            handle_help_button_click("Data Filtering Methods", "Additional data filtering methods applied")
        st.text_area(
            "Data Filtering Methods",
            key="data_filtering_methods",
            label_visibility="collapsed"
        )

        st.markdown("**Data Normalization Method**")
        st.caption("Method used for data normalization (e.g., TPM, FPKM, DESeq2)")
        if st.button("Help with Data Normalization Method", icon="🤖", key="help_data_normalization_method"):
            handle_help_button_click("Data Normalization Method", "Method used for data normalization (e.g., TPM, FPKM, DESeq2)")
        st.text_input(
            "Data Normalization Method",
            key="data_normalization_method",
            label_visibility="collapsed"
        )

        st.markdown("**Data Analysis Tools/Algorithms**")
        st.caption("Software tools and algorithms used for data analysis")
        if st.button("Help with Data Analysis Tools/Algorithms", icon="🤖", key="help_data_analysis_tools_algorithms"):
            handle_help_button_click("Data Analysis Tools/Algorithms", "Software tools and algorithms used for data analysis")
        st.text_area(
            "Data Analysis Tools/Algorithms",
            key="data_analysis_tools_algorithms",
            label_visibility="collapsed"
        )

        st.markdown("**Identifiers**")
        st.caption("Gene/transcript identifier system used (e.g., Ensembl, RefSeq)")
        if st.button("Help with Identifiers", icon="🤖", key="help_identifiers"):
            handle_help_button_click("Identifiers", "Gene/transcript identifier system used (e.g., Ensembl, RefSeq)")
        st.text_input(
            "Identifiers",
            key="identifiers",
            label_visibility="collapsed"
        )

    if st.button("Save"):
        form_data = {}
        for key in st.session_state:
            if key not in ["metadata", "messages", "agent"] and st.session_state[key]:
                form_data[key] = st.session_state[key]

        st.session_state.metadata = form_data
        st.success("Context updated!")
    
        
with col2:
    st.subheader("Assistant")

    if st.session_state.metadata:
        with st.expander("Current Metadata", expanded=False, icon="📄"):
            st.json(st.session_state.metadata)
        
    if prompt := st.chat_input("Ask for suggestions..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("Thinking..."):
            try:
                assistant_reply = st.session_state.agent.get_suggestion(
                    user_input=prompt,
                    current_metadata=st.session_state.metadata,
                    chat_history=st.session_state.messages[:-1]
                )
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": assistant_reply
                })
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": error_msg
                })
                st.error(f"Failed to get response: {str(e)}")

    with st.container(height=450, border=True):
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])
