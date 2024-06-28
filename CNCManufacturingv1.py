import streamlit as st
import pandas as pd
from fpdf import FPDF
import tempfile

# Function to generate PDF
def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Saved Inputs", ln=True, align='C')
    pdf.ln(10)

    for key, value in data.items():
        pdf.multi_cell(0, 10, txt=f"{key}: {value}")

    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    pdf.output(pdf_path.name)
    return pdf_path.name

# Streamlit app
def main():
    st.title("CNC Manufacturing Version 1")

    # Input fields
    client_id = st.text_input("Client ID")
    client_name = st.text_input("Client Name")
    job_number = st.text_input("Job Number")
    invoice_id = st.text_input("Invoice ID")
    purchase_order_id = st.text_input("Purchase Order ID")
    part_numbers = st.text_area("Part Numbers (comma-separated)")
    parts_quantities = st.text_area("Parts Quantities (comma-separated)")
    part_received_date = st.date_input("Part Received Date")
    parts_sent_date = st.date_input("Parts Sent Date")
    parts_sent_to_supplier_date = st.date_input("Parts Sent to Supplier Date")
    parts_received_by_supplier_date = st.date_input("Parts Received by Supplier Date")
    parts_received_from_supplier_date = st.date_input("Parts Received from Supplier Date")
    release_from_client_date = st.date_input("Release from Client Form Received Date")
    blanket_order_date = st.date_input("Blanket Order Date")
    client_order_date = st.date_input("Client Order Date")
    job_order_date = st.date_input("Job Order Date")
    cnc_id = st.text_input("CNC ID")
    route = st.text_area("Route (include CNC machines within route)")
    purchasing = st.text_area("Purchasing")
    payment = st.text_area("Payment")
    job_id = st.text_input("Job ID")
    measurements_of_part = st.text_area("Measurements of Part")
    gauge_of_part = st.text_input("Gauge of Part")
    quantity_of_part = st.number_input("Quantity of Part", min_value=0, step=1)
    cnc_setup_time = st.number_input("CNC Setup Time (hours)", min_value=0.0, step=0.1)
    project_completion_time = st.number_input("Time to Complete Project (hours)", min_value=0.0, step=0.1)
    number_of_machines = st.number_input("Number of Machines for Production", min_value=0, step=1)
    cleaning_cnc_time = st.number_input("Cleaning CNC Machines Time (hours)", min_value=0.0, step=0.1)
    cleaning_scrap_oil_time = st.number_input("Cleaning Scrap and Oil Time (hours)", min_value=0.0, step=0.1)
    inventory_batching = st.text_area("Inventory Batching for Shipment")
    picking_packing_units = st.text_area("Picking and Packing Units into Boxes")
    shipment_documentation = st.text_area("Documentation of Shipment to Supplier")
    notes = st.text_area("Notes")

    # Save button
    if st.button("Save Inputs"):
        data = {
            "Client ID": client_id,
            "Client Name": client_name,
            "Job Number": job_number,
            "Invoice ID": invoice_id,
            "Purchase Order ID": purchase_order_id,
            "Part Numbers": part_numbers,
            "Parts Quantities": parts_quantities,
            "Part Received Date": part_received_date,
            "Parts Sent Date": parts_sent_date,
            "Parts Sent to Supplier Date": parts_sent_to_supplier_date,
            "Parts Received by Supplier Date": parts_received_by_supplier_date,
            "Parts Received from Supplier Date": parts_received_from_supplier_date,
            "Release from Client Form Received Date": release_from_client_date,
            "Blanket Order Date": blanket_order_date,
            "Client Order Date": client_order_date,
            "Job Order Date": job_order_date,
            "CNC ID": cnc_id,
            "Route": route,
            "Purchasing": purchasing,
            "Payment": payment,
            "Job ID": job_id,
            "Measurements of Part": measurements_of_part,
            "Gauge of Part": gauge_of_part,
            "Quantity of Part": quantity_of_part,
            "CNC Setup Time (hours)": cnc_setup_time,
            "Project Completion Time (hours)": project_completion_time,
            "Number of Machines": number_of_machines,
            "Cleaning CNC Time (hours)": cleaning_cnc_time,
            "Cleaning Scrap and Oil Time (hours)": cleaning_scrap_oil_time,
            "Inventory Batching for Shipment": inventory_batching,
            "Picking and Packing Units into Boxes": picking_packing_units,
            "Shipment Documentation": shipment_documentation,
            "Notes": notes
        }

        # Save to CSV
        df = pd.DataFrame([data])
        csv_path = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        df.to_csv(csv_path.name, index=False)

        # Generate and save PDF
        pdf_path = generate_pdf(data)

        st.success("Inputs saved successfully!")

        # Provide download links
        with open(csv_path.name, "rb") as csv_file:
            st.download_button(
                label="Download CSV",
                data=csv_file,
                file_name="saved_inputs.csv",
                mime="text/csv"
            )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="saved_inputs.pdf",
                mime="application/pdf"
            )

# Run the app
if __name__ == "__main__":
    main()
