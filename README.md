# wingman-demo-agent

A tiny runnable demo showing Project Wingman wrapped around a toy agent in <30 lines.  

People don’t believe docs.  
They believe examples.  

---

What this proves  
	•	tools don’t run “because the model said so”  
	•	the Responsibility Handshake (P-04) gates execution  
	•	rollback/interrupt are not vibes — they are defaults  

---

Run  

```  
python3 demo.py  
```  

Expected behavior:  
	•	First attempt: tool call is BLOCKED   
	•	Then you perform the Responsibility Handshake  
	•	Second attempt: tool call executes  

---

Source  

Wingman primitives live here:  

https://github.com/DoctorJamesMichel/project-wingman  

---

## Example Output

```bash
python3 demo.py
-> BLOCKED: upstream responsibility not installed (P-04).

P-04 Responsibility Handshake:
I confirm I am accountable for outcomes of tool use.
Type YES to proceed: YES
[tool] searching for: reversible entanglement battery paper
```

