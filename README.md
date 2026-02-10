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
python demo.py  
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
