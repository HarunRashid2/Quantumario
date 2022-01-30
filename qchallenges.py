def q1lvl1(qkd, life):
    print("Suddenly, a wild duck appears! It speaks with a deep voice: If you wish to pass and go to your princess, you need to answer the eight Guardian Ducks' questions, Quantumario!")
    time.sleep(3)
    print("Here is the first one: What does the no cloning theorem entail?!")
    time.sleep(2)
    print("a. It is impossible to create identical copies of an arbitrary unknown quantum state")
    time.sleep(1)
    print("b. It is possible to create identical copies of quantum states, as long as they aren’t measured")
    time.sleep(1)
    print("c. No clone can last for more than a minute ")
    time.sleep(1)
    print("d. It is possible to create identical copies of quantum states.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    if qkd == True: #if you get the hint
        print("The princess says: 'It's in the name, duh!'")
    elif qkd == False: 
        print("The princess says: 'Cloning? Sounds like you should be able to create clones'") #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "a":
        print("Correct! The duck moves out of the way. You continue.")
        time.sleep(2)
        print("The path here is nice. Trees surround you, and the sun shines.")
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
        time.sleep(2)
        print("The duck disappears while you blink. You continue. The path here is nice. Trees surround you, and the sun shines.")
    time.sleep(1)
    print('...')
    os.system('cls' if os.name == 'nt' else 'clear')

def q2lvl1(qkd, life):
    time.sleep(4)
    print("The sun is suddenly blocked. A beautiful creature descends from the skies, flapping its wings. The duck speaks shrilly: Which one of these isn't a real QKD protocol?")
    time.sleep(1)
    print("a. BB84")
    time.sleep(1)
    print("b. T95")
    time.sleep(1)
    print("c. SSP99")
    time.sleep(1)
    print("d. SARG04")
    time.sleep(2)
    if qkd == True: #if you get the hint
        print("The princess says: 'I’ve heard of SARG04 before…'")
    elif qkd == False: 
        print("The princess says: 'I’ve heard of T95 before…'") #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "b":
        print("Correct! The duck gives way, and you continue.")
        time.sleep(2)
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
        time.sleep(2)
    print("The trees start to clear, hills take their place.")
    print("Another Toad stands at a quantum device ahead of you.")
    time.sleep(2)
    print("Hey Mario! You should create a new key, the old one doesn't work in the wastelands up ahead!") 
        
    #Another QKD challenge, needs code

    time.sleep(1)
    print('...')
    os.system('cls' if os.name == 'nt' else 'clear')
    
def q1lvl2(qkd, life):
    time.sleep(3)
    print("The ground shakes. A creature tall as a mountain towers before you. From up above, the beak moves and you hear its thunderous voice ask: Which one of these QKD protocols utilizes quantum entanglement?")
    time.sleep(1)
    print("a. SSP99")
    time.sleep(1)
    print("b. SARG04")
    time.sleep(1)
    print("c. Eckert's Protocol")
    time.sleep(1)
    print("d. B92")
    time.sleep(1)
    if qkd == True: #if you get the hint
        print("The princess says: 'Well that one has words at least…'")
    elif qkd == False: 
        print("The princess says: 'I have no idea'") #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "c":
        print("Correct! The huge duck takes flight, leaving way for you. You continue")
        time.sleep(2)
        print("
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
        time.sleep(2)
        print("The huge duck takes flight, leaving way for you. You continue") 
        time.sleep(2)
        print("The world switches around you. The green grass disappears, leaving way for a desolate wasteland.")
        time.sleep(2)
        
    time.sleep(1)
    print('...')
    os.system('cls' if os.name == 'nt' else 'clear')

def q2lvl2(qkd, life):
    time.sleep(4)
    print("A duck sized duck stops your way. The duck asks you: What is quantum teleportation?")
    time.sleep(1)
    print("a. Communicating using entangled states and a classical information channel")
    time.sleep(1)
    print("b. Being able to teleport to one of two places, not knowing which one of them you'll end up at.")
    time.sleep(1)
    print("c. Teleporting objects and states using a quantum computer")
    time.sleep(1)
    print("d. Communicating using classical bits.")
    time.sleep(1)
    if qkd == True: #if you get the hint
        print("The princess says: Classical bits has nothing to do with teleportation, right?")
    elif qkd == False: 
        print("The princess says: Wow, teleportation") #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "a":
        print("Correct! The duck moves to the side, and you continue through the wasteland.")
        time.sleep(2)
        print("After yet some time, you see another Toad, with yet another Quantum Computer.")
        time.sleep(2)
        print("Hey Mario. You need to redo the key once more before you arrive at the castle.") 
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
    time.sleep(1)
    print("The duck moves to the side, and you continue through the wasteland.")
    time.sleep(3)
    print("After yet some time, you see another Toad, with yet another Quantum Computer.")
    time.sleep(2)
    print("Hey Mario, the Toad says. You need to redo the key once more before you arrive at the castle.")  #Needs code again
    time.sleep(1)
    print('...')

def q1lvl3(qkd, life):
    time.sleep(3)
    print("A cold wind sends a chill through your spine. It carries a faint whisper, asking: What is a PNS attack?")
    time.sleep(2)
    print("a. Peripheral Nervous System attack, an attack on the nervous system.")
    time.sleep(1)
    print("b. Photons Number Splitter attack, where an eavesdropper can steal photons from a quantum channel.")
    time.sleep(1)
    print("c. Probably Not Something nice.")
    time.sleep(1)
    print("d. Premium Neutron Splitter attack, an attack with a neutron splitter which can distrupt a quantum channel")
    time.sleep(1)
    if qkd == True: #if you get the hint
        print("The princess says: Surely it's quantum related...")
    elif qkd == False: 
        print("The princess says: It's probably not something nice. ") #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "b":
        print("Correct! You continue")
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
    time.sleep(1)
    print('...')
    os.system('cls' if os.name == 'nt' else 'clear')
    
def q2vl3(qkd, life):
    time.sleep(3)
    print("A duck digs its way to the surface to greet you. It is a cyborg duck. It asks you in its robotic voice: How do you create entanglement in the simplest way possible?")
    time.sleep(2)
    print("a. With a Hadamard gate.")
    time.sleep(1)
    print("b. With a Pauli-X gate on the first qubit, and a Pauli-Z gate on the second.")
    time.sleep(1)
    print("c. With a Hadamard gate on the first qubit, then a CNOT with the first qubit as the control qubit and the second qubit as the target.")
    time.sleep(1)
    print("d. With a CNOT with the second qubit as the control qubit and the first as the target qubit.")
    time.sleep(1)
    if qkd == True: #if you get the hint
        print("The princess says: You need at least two qubits to create entanglement.")
    elif qkd == False: 
        print("The princess says: Wow, this is too advanced for me.") #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "c":
        print("Correct!") 
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
    time.sleep(1)
    print("You continue. A castle spire is visible far away.")
    time.sleep(1)
    print('...')
    os.system('cls' if os.name == 'nt' else 'clear')
              
              
#q1lvl4
              
def q1lvl4(qkd, life):
    time.sleep(3)
    print("A dark storm arises, carrying hail and wind. A faint outline of a winged creature is visible in front of you. It looks almost mythical. It let's out a screech and asks. 'What are pure quantum states?'")
    time.sleep(2)
    print("a. Quantum states formed after superposition")
    time.sleep(1)
    print("b. Vectors in a Euler space, associated with Laplace operator.")
    time.sleep(1)
    print("c.  Particles made in clean room.")
    time.sleep(1)
    print("d. Vectors in a Hilbert space, while each observable quantity is associated with a mathematical operator..")
    time.sleep(1)
    if qkd == True: #if you get the hint
        print("The princess says: vectors maybe?...")
    elif qkd == False: 
        print("The princess says: ..come on!!) #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "d":
        print("Correct!")
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
    time.sleep(2)
    print("You struggle on through the storm
    time.sleep(1)
    print('...')
    os.system('cls' if os.name == 'nt' else 'clear')             

#q2lvl4
def q2lvl4(qkd, life):
    time.sleep(3)
    print("You have finally reached the gate.")
    time.sleep(3)
    print("One last guradian awaits you.")
    time.sleep(3)
    print("A duck the size of small bird sits on the footsteps of the gate.")
    time.sleep(3)
    print("'You have done well so far Mario', says the duck. 'But there is still one more question left for you to answer. Now tell me: Which of these alternatives are a step in the process of Quantum Key Distribution?")
    time.sleep(2)
    print("a. The sender sends a photon through a polarizer with randomly assigned polarizations and bit assignment.")
    time.sleep(1)
    print("b. Photon uses a beam splitter that can be horizontal, vertical, or diagonal to decode or read the polarization of each photon.")
    time.sleep(1)
    print("c. Receiver tells the sender the random assignments of a beam splitter for each photon in the same sequence it was sent.")
    time.sleep(1)
    print("d. All of the above.")
    time.sleep(1)
    if qkd == True: #if you get the hint
        print("The princess says: 'I'm pretty sure that I've heard of option a before...")
    elif qkd == False: 
        print("The princess says: I have no clue!") #bowser hint
    time.sleep(2)
    q1ans=input("What is your answer?")
    if q1ans == "d":
        print("Correct!")
    else:
        print("Wrong! You lose a life but you must keep moving...")
        return life - 1
    time.sleep(2)
    print("You enter the castle, and brace yourself for one final challenge")
    time.sleep(1)
    print('...')
    os.system('cls' if os.name == 'nt' else 'clear')  


    
    
