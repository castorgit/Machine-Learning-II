# Frequently Asked Questions (FAQ)

## General Questions

### Q: What are the prerequisites for this course?
**A:** You should have completed Machine Learning I or equivalent, have strong Python programming skills, and understand linear algebra, calculus, and probability/statistics.

### Q: What programming language is used in this course?
**A:** All coursework is in Python 3.8 or higher. We use popular ML libraries like TensorFlow, PyTorch, and scikit-learn.

### Q: Do I need a powerful computer for this course?
**A:** While a GPU is helpful, it's not required. You can use:
- Google Colab (free GPU access)
- University computing resources
- Cloud platforms (AWS, GCP, Azure)
- Your own computer for smaller datasets

## Setup and Installation

### Q: How do I set up my environment?
**A:** Follow these steps:
```bash
# Clone the repository
git clone https://github.com/castorgit/Machine-Learning-II.git
cd Machine-Learning-II

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Q: I'm having trouble installing TensorFlow/PyTorch. What should I do?
**A:** 
- Check your Python version (3.8-3.11 recommended)
- For GPU support, install CUDA and cuDNN first
- Try installing CPU-only versions initially
- Use conda instead of pip if issues persist
- Check the official documentation for your OS

### Q: Can I use Jupyter Lab instead of Jupyter Notebook?
**A:** Yes! Both are supported. Install with: `pip install jupyterlab`

## Assignments and Labs

### Q: Where do I submit my assignments?
**A:** Submit assignments through Pull Requests to your forked repository. See CONTRIBUTING.md for detailed instructions.

### Q: Can I use external libraries not in requirements.txt?
**A:** Yes, but:
- Document them in your assignment README
- Add them to a separate requirements file for your submission
- Ensure they don't violate course policies on implementing core algorithms

### Q: How much collaboration is allowed?
**A:** 
- Discussion of concepts: ✅ Encouraged
- Sharing ideas and approaches: ✅ Allowed
- Copying code: ❌ Not allowed
- Working on code together: ❌ Not allowed
- Using online resources: ✅ Allowed (with citation)

### Q: I'm stuck on an assignment. Where can I get help?
**A:** 
1. Review lecture materials and notebooks
2. Check documentation for libraries you're using
3. Search for similar issues online (Stack Overflow, etc.)
4. Attend office hours
5. Post in the course discussion forum
6. Email the instructor/TA

### Q: Can I submit assignments late?
**A:** Yes, with a penalty: -10% per day for up to 3 days. After 3 days, contact the instructor for special circumstances.

## Technical Issues

### Q: My notebook kernel keeps dying. What should I do?
**A:** 
- You might be running out of memory
- Try reducing batch size or dataset size
- Restart the kernel and clear outputs
- Close other applications
- Use Google Colab for more resources

### Q: I get "CUDA out of memory" errors. How do I fix this?
**A:** 
- Reduce batch size
- Use gradient accumulation
- Clear CUDA cache: `torch.cuda.empty_cache()`
- Use mixed precision training
- Switch to CPU for testing (slower but works)

### Q: My model is training too slowly. Any tips?
**A:** 
- Use GPU acceleration
- Reduce model complexity for testing
- Use data augmentation efficiently
- Implement data loading in parallel
- Use smaller datasets initially
- Consider using pre-trained models

## Course Content

### Q: Where can I find additional resources?
**A:** Check the `/resources` directory for:
- Research papers
- Tutorial links
- Recommended readings
- Tool setup guides

### Q: Will there be solutions provided?
**A:** Sample solutions may be provided after the assignment deadline has passed and all submissions are received.

### Q: Can I use pre-trained models?
**A:** Depends on the assignment:
- Transfer learning assignments: Yes, that's the goal
- Implementation assignments: No, implement from scratch
- Check assignment instructions carefully

### Q: What's the difference between PyTorch and TensorFlow?
**A:** Both are deep learning frameworks:
- **TensorFlow**: Google's framework, Keras integration, strong deployment tools
- **PyTorch**: Facebook's framework, more Pythonic, popular in research
- **For this course**: Learn both! Different assignments may use different frameworks

## Projects

### Q: Can I choose my own project topic?
**A:** Yes! Projects should:
- Demonstrate course concepts
- Be appropriately scoped (achievable in timeframe)
- Use real-world datasets
- Be approved by instructor

### Q: Can I work in groups for the final project?
**A:** Check the syllabus. Typically, groups of 2-3 are allowed with instructor approval.

### Q: What makes a good project?
**A:** 
- Clear problem statement
- Appropriate dataset
- Multiple approaches tried
- Thorough evaluation
- Good documentation
- Interesting insights

## Grading

### Q: How are assignments graded?
**A:** Based on:
- Correctness (50%)
- Code quality (20%)
- Documentation (15%)
- Results analysis (15%)

### Q: Can I resubmit if I'm not satisfied with my grade?
**A:** Contact the instructor. Resubmissions may be allowed for partial credit in special cases.

### Q: I think there's an error in my grading. What should I do?
**A:** Submit a regrade request within one week of receiving your grade, with a clear explanation of the issue.

## Miscellaneous

### Q: Will this course help me get a job in ML/AI?
**A:** This course provides strong theoretical and practical foundations. Combine it with:
- Personal projects
- Contributions to open source
- Kaggle competitions
- Internships
- Building a portfolio

### Q: What should I do after this course?
**A:** Consider:
- Advanced courses (NLP, Computer Vision, Reinforcement Learning)
- Research projects
- Industry internships
- Kaggle competitions
- Reading recent papers
- Building portfolio projects

### Q: How can I stay updated with the latest in ML?
**A:** 
- Follow AI conferences (NeurIPS, ICML, CVPR)
- Read ArXiv papers
- Follow ML researchers on Twitter/LinkedIn
- Join ML communities
- Take advanced online courses
- Participate in reading groups

---

**Still have questions?** Contact the course instructor or post in the discussion forum!
