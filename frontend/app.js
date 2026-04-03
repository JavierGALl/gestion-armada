const API_URL = 'http://127.0.0.1:8000/api/funcionarios/';
const TECH_URL = 'http://127.0.0.1:8000/api/tecnologias/'; // Asegúrate de tener esta ruta

let isEditing = false;

// 1. CARGAR TECNOLOGÍAS (Checkboxes)
async function cargarTecnologias() {
    const res = await fetch(TECH_URL);
    const techs = await res.json();
    const container = document.getElementById('tech-checkboxes');
    container.innerHTML = techs.map(t => `
        <div class="form-check">
            <input class="form-check-input tech-check" type="checkbox" value="${t.id}" id="tech-${t.id}">
            <label class="form-check-label" for="tech-${t.id}">${t.nombre}</label>
        </div>
    `).join('');
}

// 2. LISTAR FUNCIONARIOS
async function cargarFuncionarios() {
    const res = await fetch(API_URL);
    const data = await res.json();
    const tabla = document.getElementById('lista-funcionarios');
    tabla.innerHTML = data.map(f => `
        <tr>
            <td>${f.nombre_completo}</td>
            <td><span class="badge bg-info text-dark">${f.grado}</span></td>
            <td>${f.tecnologias_detalle.map(t => t.nombre).join(', ')}</td>
            <td>
                <button class="btn btn-warning btn-sm" onclick="prepararEdicion(${f.id})">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="eliminarFuncionario(${f.id})">Eliminar</button>
            </td>
        </tr>
    `).join('');
}

// 3. PREPARAR EDICIÓN (Cargar datos al form)
async function prepararEdicion(id) {
    const res = await fetch(`${API_URL}${id}/`);
    const f = await res.json();

    document.getElementById('nombre').value = f.nombre_completo;
    document.getElementById('rut').value = f.rut;
    document.getElementById('grado').value = f.grado;
    document.getElementById('editing-id').value = f.id;

    // Marcar los checkboxes que ya tiene el funcionario
    document.querySelectorAll('.tech-check').forEach(check => {
        check.checked = f.tecnologias.includes(parseInt(check.value));
    });

    document.querySelector('button[type="submit"]').textContent = "Actualizar Cambios";
    document.querySelector('button[type="submit"]').className = "btn btn-primary w-100";
    isEditing = true;
}

// 4. GUARDAR O ACTUALIZAR
document.getElementById('registro-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const selectedTechs = Array.from(document.querySelectorAll('.tech-check:checked')).map(c => parseInt(c.value));

    const datos = {
        nombre_completo: document.getElementById('nombre').value,
        rut: document.getElementById('rut').value,
        grado: document.getElementById('grado').value,
        tecnologias: selectedTechs,
        activo: true
    };

    const url = isEditing ? `${API_URL}${document.getElementById('editing-id').value}/` : API_URL;
    const method = isEditing ? 'PUT' : 'POST';

    await fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    });

    resetForm();
    cargarFuncionarios();
});

function resetForm() {
    document.getElementById('registro-form').reset();
    document.getElementById('editing-id').value = "";
    document.querySelector('button[type="submit"]').textContent = "Guardar";
    document.querySelector('button[type="submit"]').className = "btn btn-success w-100";
    isEditing = false;
}

async function eliminarFuncionario(id) {
    if (confirm('¿Desea eliminar este registro naval?')) {
        await fetch(`${API_URL}${id}/`, { method: 'DELETE' });
        cargarFuncionarios();
    }
}

// Inicializar
cargarTecnologias();
cargarFuncionarios();