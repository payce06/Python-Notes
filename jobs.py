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
