class StudentGWAAnalyzer:
    """
    Analyzes students.txt to find student with HIGHEST GWA (1.00 = BEST).
    REQUIRES existing students.txt file with format: "Name GWA"
    """

    def __init__(self, filename: str = "students.txt"):
        self.filename = filename
        self.students = []

    def analyze(self) -> None:
        print("STUDENT GWA ANALYZER")
        print("*" * 60)

        # Step 1: Load students
        self._load_students()

        # Step 2: Finding the top student
        top_student = self._find_top_student()

        # Step 3: Displaying results
        self._display_results(top_student)

    def _load_students(self) -> None:
        try:
            with open(self.filename, 'r') as file:
                self.students = []
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue

                    parts = line.rsplit(maxsplit=1)  # Split from right, max 1 split
                    if len(parts) != 2:
                        continue

                    name, gwa_str = parts
                    try:
                        gwa = float(gwa_str)
                        if 1.0 <= gwa <= 4.0:  # GWA range 1.0-4.0
                            self.students.append({"name": name.strip().title(), "gwa": gwa})
                    except ValueError:
                        pass

                if not self.students:
                    raise ValueError("No valid students found!")

                print(f"Loaded {len(self.students)} students from {self.filename}")

        except FileNotFoundError:
            print(f"ERROR: '{self.filename}' not found!")
            print("Create students.txt with format: 'Name GWA'")
            raise
        except Exception as e:
            print(f"Error reading file: {e}")
            raise

    def _find_top_student(self) -> dict:
        # Use min() since we want the 1.00 be the highest possible GWA
        return min(self.students, key=lambda x: x["gwa"])

    def _display_results(self, top_student: dict) -> None:
        print(f"TOP STUDENT: {top_student['name']}")
        print(f"GWA:   {top_student['gwa']:.2f}")
        print(f"Rank:  1st out of {len(self.students)} students")

def main():
    try:
        analyzer = StudentGWAAnalyzer("students.txt")
        analyzer.analyze()
        print("Analysis complete!")
    except Exception as e:
        print("Check your students.txt file format!")


if __name__ == "__main__":
    main()