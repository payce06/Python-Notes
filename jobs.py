class JobPosting:
    def __init__(self, job_title, job_id, company_name, skills_required):
        """Initialize the JobPosting object."""
        self.job_title = job_title
        self.job_id = job_id
        self.company_name = company_name
        self.skills_required = skills_required
        self.applicants = []

    def add_applicant(self, engineer):
        """Add an applicant to the job posting."""
        if engineer not in self.applicants:
            self.applicants.append(engineer)
            print(f"{engineer.name} applied for {self.job_title} at {self.company_name}.")
        else:
            print(f"{engineer.name} has already applied for {self.job_title} at {self.company_name}.")

def display_applicants(self):
        """Display all applicants for the job."""
        print(f"Job: {self.job_title} at {self.company_name} (ID: {self.job_id})")
        print("Applicants:")
        for applicant in self.applicants:
            print(f"- {applicant.name} (ID: {applicant.engineer_id})")

class SoftwareEngineer:
    def __init__(self, name, engineer_id, skills):
        """Initialize the SoftwareEngineer object."""
        self.name = name
        self.engineer_id = engineer_id
        self.skills = skills
        self.applications = []  # List of applied job IDs

    def apply_to_job(self, job_posting):
        """Apply for a job."""
    
    
        if job_posting.job_id not in self.applications:
            job_posting.add_applicant(self)
            self.applications.append(job_posting.job_id)
        else:
            print(f"{self.name} has already applied for {job_posting.job_title} at {job_posting.company_name}.")

    def display_profile(self):
        """Display the engineer's profile."""
        print(f"Engineer ID: {self.engineer_id}")
        print(f"Name: {self.name}")
        print("Skills: " + ", ".join(self.skills))
        print("Applied Jobs:")
        for job_id in self.applications:
            print(f"- Job ID: {job_id}")

class JobApplicationSystem:
    def __init__(self):