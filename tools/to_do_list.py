import streamlit as st
import datetime
import cohere

# Streamlit app layout
st.set_page_config(page_title="To-Do List with AI Task Insights", page_icon="📝")
st.title("📝 To-Do List with AI Task Insights")
st.markdown("Keep track of your daily tasks, prioritize effectively, and get AI-powered task insights.")

# Input API key for Cohere
api_key = st.text_input("Enter your Cohere API Key", type="password")

# Initialize the task list in session state
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Input fields for new task
task_name = st.text_input("Task Name")
task_priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=1)
due_date = st.date_input("Due Date", datetime.date.today())

# Button to add a new task
if st.button("Add Task"):
    if task_name.strip():
        st.session_state['tasks'].append({
            'Task': task_name.strip(),
            'Priority': task_priority,
            'Due Date': due_date,
            'Created On': datetime.date.today()
        })
        st.success(f"✅ Task '{task_name}' added successfully!")
    else:
        st.warning("⚠️ Please enter a valid task name.")

# Display the task list
if st.session_state['tasks']:
    st.subheader("Your Tasks")
    tasks_df = st.session_state['tasks']
    sorted_tasks = sorted(tasks_df, key=lambda x: (x['Priority'], x['Due Date']))
    task_summaries = []
    for task in sorted_tasks:
        task_text = f"📌 **{task['Task']}** - {task['Priority']} Priority (Due: {task['Due Date']})"
        st.write(task_text)
        task_summaries.append(f"{task['Task']} ({task['Priority']} priority, due {task['Due Date']})")
    
    # Generate task insights using Cohere if API key is provided
    if api_key:
        try:
            co = cohere.Client(api_key)
            prompt = ("Generate a task management summary based on the following tasks:\n" + "\n".join(task_summaries))
            response = co.generate(
                model="command-xlarge",
                prompt=prompt,
                max_tokens=300,
                temperature=0.7,
                k=0,
                p=0.8,
                frequency_penalty=0.2,
                presence_penalty=0.2
            )
            if response.generations:
                insights = response.generations[0].text.strip()
                st.subheader("AI Task Insights:")
                st.write(insights)
            else:
                st.warning("⚠️ No insights generated. Try again later.")
        except Exception as e:
            st.error(f"Error generating insights: {str(e)}")
else:
    st.info("No tasks added yet. Stay organized and add your first task!")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Cohere")
