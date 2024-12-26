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
    
    
        """Initialize the Job Application System."""
        self.engineers = {}
        self.job_postings = {}

    def add_engineer(self, engineer):
        """Add an engineer to the system."""
        if engineer.engineer_id not in self.engineers:
            self.engineers[engineer.engineer_id] = engineer
            print(f"Engineer {engineer.name} added to the system.")
        else:
            print(f"Engineer ID {engineer.engineer_id} already exists.")

    def add_job_posting(self, job_posting):
        """Add a job posting to the system."""
        if job_posting.job_id not in self.job_postings:
    
    
            self.job_postings[job_posting.job_id] = job_posting
            print(f"Job {job_posting.job_title} at {job_posting.company_name} added to the system.")
        else:
            print(f"Job ID {job_posting.job_id} already exists.")

    def display_all_jobs(self):
        """Display all job postings."""
        for job in self.job_postings.values():
            print(f"{job.job_title} at {job.company_name} (ID: {job.job_id}) - Skills Required: {', '.join(job.skills_required)}")

    def display_all_engineers(self):
        """Display all engineers in the system."""
        for engineer in self.engineers.values():
            engineer.display_profile()

# Main Program
if __name__ == "__main__":
    # Create the job application system

    
    system = JobApplicationSystem()

    # Create job postings
    job1 = JobPosting("Software Engineer", "JOB101", "TechCorp", ["Python", "Django", "SQL"])
    job2 = JobPosting("Frontend Developer", "JOB102", "Webify", ["JavaScript", "React", "CSS"])

    # Add job postings to the system
    system.add_job_posting(job1)
    system.add_job_posting(job2)

    # Create software engineers
    engineer1 = SoftwareEngineer("Alice Johnson", "ENG123", ["Python", "Django", "Flask"])
    engineer2 = SoftwareEngineer("Bob Smith", "ENG456", ["JavaScript", "React", "Node.js"])

    # Add engineers to the system
    system.add_engineer(engineer1)
    system.add_engineer(engineer2)

    # Engineers apply for jobs
    engineer1.apply_to_job(job1)
    engineer1.apply_to_job(job2)
    engineer2.apply_to_job(job2)