export default function getListStudentIds(studentIDs) {
  if (!Array.isArray(studentIDs)) {
    return [];
  }
  return studentIDs.map((studentIDs) => studentIDs.id);
}
