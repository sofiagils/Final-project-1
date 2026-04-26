from PyQt6.QtWidgets import QMainWindow
from gui import Ui_MainWindow
import os
import csv

class Logic(QMainWindow, Ui_MainWindow):
    CSV_FILE_PATH = "./votes_db.csv"
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_vote_button.clicked.connect(lambda: self.save_vote())

    def save_vote(self):
        voter_id = self.get_voter_id()
        voter_id_error_msg = self.validate_voter_id(voter_id)
        if voter_id_error_msg:
            self.update_validation_label(voter_id_error_msg, 'red')
            return
        
        candidate = self.get_candidate()
        candidate_error_msg = self.validate_candidate(candidate)
        if candidate_error_msg:
            self.update_validation_label(candidate_error_msg, 'red')
            return
        
        previous_vote_error_msg = self.validate_previous_votes(voter_id)
        if previous_vote_error_msg:
            self.update_validation_label(previous_vote_error_msg, 'red')
            return

        if os.path.isfile(Logic.CSV_FILE_PATH):
            self.update_csv_file(voter_id, candidate)
        else:
            self.create_csv_file(voter_id, candidate)
        
        self.update_validation_label("Vote saved!", 'green')

        



    def get_candidate(self):
        if self.candidate_1_radio_button.isChecked():
            return self.candidate_1_radio_button.text()
        elif self.candidate_2_radio_button.isChecked():
            return self.candidate_2_radio_button.text()

    def validate_candidate(self, candidate):
        if not candidate:
            return "Select one candidate"

    def get_voter_id(self):
        return self.voter_id_input.text()

    def validate_voter_id(self, voter_id):
        if len(voter_id) != 9:
            return "ID should be 9 digits long"
        
    def update_validation_label(self, message, color):
        self.validation_label.setText(message)
        self.validation_label.setStyleSheet(f"color: {color};")

    def create_csv_file(self, voter_id, candidate):
        with open(Logic.CSV_FILE_PATH, 'w', newline='') as votes_db_file:
            writer = csv.writer(votes_db_file)
            writer.writerows([
                ["Voter ID", "Candidate"],
                [voter_id, candidate]
            ])

    def update_csv_file(self, voter_id, candidate):
        with open(Logic.CSV_FILE_PATH, 'a', newline='') as votes_db_file:
            writer = csv.writer(votes_db_file)
            writer.writerow([voter_id, candidate])


    def get_previous_voters(self):
        with open(Logic.CSV_FILE_PATH) as votes_db_file:
            reader = csv.reader(votes_db_file)
            return [] #finish
                

    def validate_previous_votes(self, voter_id):
        if not os.path.isfile(Logic.CSV_FILE_PATH):
            return 
        previous_voters_ids = self.get_previous_voters()
        if voter_id in previous_voters_ids:
            return "Already voted"
            


        


