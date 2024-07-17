import gradio as gr
from crew import SkillCrew
from fpdf import FPDF

# Define a function to create a PDF
def create_pdf(job_title, salary_range, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add content to PDF
    pdf.cell(200, 10, txt="Smart Job Navigator Result", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Job Title: {job_title}", ln=True)
    pdf.cell(200, 10, txt=f"Salary Range: {salary_range}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=result)

    # Save the PDF to a file
    output_file = "result.pdf"
    pdf.output(output_file)
    return output_file

# Define a function that Gradio will use
def crewai_interaction(job_title, salary_range):
    crew = SkillCrew(job_title, salary_range)
    result = crew.run()

    # Create the PDF and get the file path
    pdf_file_path = create_pdf(job_title, salary_range, result)
    return pdf_file_path

# Create the Gradio interface
interface = gr.Interface(
    fn=crewai_interaction,  # The function to be called
    inputs=[
        gr.Textbox(lines=1, placeholder="Enter job title, e.g., Data Scientist", label="Job Title"),
        gr.Textbox(lines=1, placeholder="Enter salary range, e.g., $50,000 - $100,000", label="Salary Range")
    ],  # Types of input widgets
    outputs=gr.File(label="Download your roadmap as PDF"),  # Output as a file download
    title="Smart Job Navigator",  # Title of the app
    description="Personal career development app to secure a highly paid job"  # Description of the app
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()