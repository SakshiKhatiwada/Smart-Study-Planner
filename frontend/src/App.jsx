import { useState } from 'react'
import './App.css'

function App() {

  // const [id, setId] = useState(0);
  const [tasks, setTasks] = useState([]);
  const [taskDescription, setTaskDescription] = useState("");
  // var tasks = [
  //   {"id": 1, "title": "finish simple to-do app"},
  //   {"id": 2, "title": "make an MVP"},
  // ];

  var taskItems = tasks.map(task => 
    <li key={task.id}>
    <input type="checkbox" name={task.title} id={task.id} switch onChange={(e) => handleToggleTask(task.id, e.target.checked)}/>
    <label htmlFor={task.id} style={{textDecoration: task.completed? "line-through": "none"}}>{task.title}</label>
    </li>
  );

  function handleToggleTask(id, isChecked) {
  setTasks(prevTasks =>
    prevTasks.map(task =>
      task.id === id
        ? { ...task, completed: isChecked }
        : task
    )
  );
}

  // function handleSetId(){
  //   setId(id+1);
  // }

  function handleSetTask(task){
    // handleSetId(); // Bug 2, id estari update garne bittikai state update bhayeko hudaina tei block ko laagi. tala old id nai use garxa
    // setTasks(tasks.append(
    //   {
    //     "id": id,
    //     "title": task
    //   }
    // )); // Bug 1

    setTasks([...tasks, {
       "id": Date.now(),
       "title": task,
       "completed": false
    }]) // spread operator, old tasks jastaako testai lyauxa
  }

  function handleAddTask(){
    handleSetTask(taskDescription);
    setTaskDescription("");
  }

  return (<main> 
    <form>
      <input className="input-task" type="text" placeholder='Enter your task'
      value={taskDescription}
      onChange={(e) => setTaskDescription(e.target.value)} 
      />
      <button type="button" onClick={handleAddTask}>Add Task</button>
    </form>

    <div>
      <ul>
        {taskItems}
      </ul>
    </div>

  </main>);
  }

export default App
