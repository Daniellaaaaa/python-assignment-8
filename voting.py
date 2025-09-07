# """
# TASK: Create a VotingSystem class.

# Requirements:
# 1. The class should allow registering candidates.
# 2. Each candidate should start with 0 votes.
# 3. The class should allow voters (using voter IDs) to cast votes.
#    - Ensure one voter cannot vote more than once.
# 4. Provide a method to display election results.

# Example Usage:
#     election = VotingSystem()
#     election.register_candidate("Alice")
#     election.register_candidate("Bob")
#     election.vote("Voter1", "Alice")
#     election.vote("Voter2", "Bob")
#     election.vote("Voter3", "Alice")
#     print(election.results())  # {"Alice": 2, "Bob": 1}
#     print(election.winner()) # Alice
# """

class VotingSystem:
    def __init__(self):
        self.candidates={}
        self.voters=set()

        
    def register_candidate(self, name):
        if name not in self.candidates:
            self.candidates[name]=0
            return f"Candidate {name} registered successfully"
        else:
            return f"Candidate {name} already registered"
        
    def vote(self, voter_name, candidate_name):
        if voter_name not in self.voters:
            self.candidates[candidate_name]+=1
            self.voters.add(voter_name)
            return f"{voter_name} has voted for {candidate_name} successfully"
        else:
            return f"{voter_name} has already voted"
        

    def winners(self):
        max_vote=0
        winner=[]

        for candidates, votes in self.candidates.items():
            if votes > max_vote:
                max_vote=votes
                winner=[candidates]
            elif votes == max_vote:
                winner.append(candidates) 

        return f"Winners: {winner}"        

        
    def results(self):
        return f"Candidates: {self.candidates}"    




election = VotingSystem()
print(election.register_candidate("Alice"))
print(election.register_candidate("Bob"))

print(election.vote("Voter1", "Alice"))
print(election.vote("Voter2", "Bob"))
print(election.vote("Voter3", "Alice"))
print(election.vote("Voter4", "Bob"))

print(election.results())  # {"Alice": 2, "Bob": 1}
print(election.winners()) # Alice
