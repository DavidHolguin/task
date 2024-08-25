import { useEffect, useState } from "react";
import { getAllTasks } from "../api/task.api";
import { TaskCard } from "./TaskCard";

export function TaskList() {
    const [tasks, setTasks] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function loadTasks() {
            try {
                const res = await getAllTasks();
                console.log("Tasks received in component:", res.data);
                
                // Asegurarse de que cada tarea tenga una descripción
                const tasksWithDescription = res.data.map(task => ({
                    ...task,
                    description: task.description || 'No description available'
                }));
                
                setTasks(tasksWithDescription);
            } catch (err) {
                console.error("Error loading tasks:", err);
                setError("Failed to load tasks. Please try again later.");
            }
        }
        loadTasks();
    }, []);

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div className="grid grid-cols-3 gap-3">
            {tasks.map(task => (
                <TaskCard key={task.id} task={task} />
            ))}
        </div>
    );
}