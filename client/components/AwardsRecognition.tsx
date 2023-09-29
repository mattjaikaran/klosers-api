import useAxios from '@/lib/utils/axios';
import { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import EditAwardRecognitionForm from './forms/stats/EditAwardRecognitionForm';
import NewAwardRecognitionForm from './forms/stats/NewAwardRecognitionForm';

const AwardsRecognition = () => {
  const api = useAxios();
  const [show, setShow] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [awards, setAwards] = useState([
    {
      id: '1',
      name: '🏆 Top revenue producer in Q1 2023, 145% quota attainment',
    },
    {
      id: '2',
      name: '🌴 Presidents Club winner 2021',
    },
    {
      id: '3',
      name: '💰 Top earner 2020 Add award & recognition',
    },
  ]);

  // Add modal
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  // Edit modal
  const handleCloseEditModal = () => setShowEditModal(false);
  const handleShowEditModal = () => setShowEditModal(true);

  // useEffect(() => {
  //   const getAwards = async () => {
  //     try {
  //       const response = await api.get(`/awards`);
  //       console.log('response getAwards', response);
  //       console.log('response.data getAwards', response.data);
  //       setAwards(response.data)
  //       return response
  //     } catch (error) {
  //       console.error('error', error);
  //     }
  //   };
  //   getAwards();
  // }, []);

  const renderAwards = () => {
    if (awards) {
      return awards.map((award: any) => (
        <p key={award.id}>
          <Button variant="link" onClick={handleShowEditModal}>
            Edit
          </Button>
          {award.name}
        </p>
      ));
    }
  };

  return (
    <div className="mt-3">
      <h5>Awards &amp; Recognition</h5>
      {renderAwards()}

      <Button
        className="mt-3 pill-btn"
        variant="outline-primary"
        onClick={handleShow}
      >
        Add Award
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add Career Stat</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <NewAwardRecognitionForm closeModal={handleClose} />
        </Modal.Body>
      </Modal>
      <Modal show={showEditModal} onHide={handleCloseEditModal}>
        <Modal.Header closeButton>
          <Modal.Title>Edit Awards &amp; Recognition Stat</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <EditAwardRecognitionForm
            id={'123'}
            closeModal={handleCloseEditModal}
          />
        </Modal.Body>
      </Modal>
    </div>
  );
};

export default AwardsRecognition;
